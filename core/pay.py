from core.order_api import *
from core.tasks import * 
from django.conf import settings 

@csrf_exempt
def pay(request):
  if settings.TEST_LIQPAY:
    sandbox = 1 
  else:
    sandbox = 0
  order = Order.objects.filter(sk=get_sk(request), ordered=False)
  if not order.exists():
    return redirect('/')
  CURRENT_DOMEN = settings.CURRENT_DOMEN
  order = order.first()
  total_price = 0
  seats_in_order = SeatInOrder.objects.filter(order=order)
  for seat_in_order in seats_in_order:
    print(seat_in_order)
    total_price += seat_in_order.race.price
  params = {
      'action': 'pay',
      'amount': float(total_price),
      'currency': 'UAH',
      'description': str(f"{order.full_name}, {order.race}"),
      # 'order_id': str(order.id+1000),
      'order_id': str(order.id),
      'version': '3',
      'sandbox': sandbox,  # sandbox mode, set to 1 to enable it
      'server_url': f'{CURRENT_DOMEN}pay_callback/', # url to callback view
  }
  liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
  signature = liqpay.cnb_signature(params)
  data = liqpay.cnb_data(params)
  return render(request, 'payment.html', {'signature': signature, 'data': data})


@csrf_exempt
def pay_callback(request):
    print('pay callback')
    liqpay    = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    data      = request.POST.get('data')
    signature = request.POST.get('signature')
    sign      = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
    response  = liqpay.decode_data_from_str(data)
    if sign == signature: print('callback is valid')
    print(response)

    action              = response.get('action', '')
    payment_id          = response.get('payment_id', '')
    status              = response.get('status', '')
    version             = response.get('version', '')
    type                = response.get('type', '')
    paytype             = response.get('paytype', '')
    public_key          = response.get('public_key', '')
    acq_id              = response.get('acq_id', '')
    order_id            = response.get('order_id', '')
    liqpay_order_id     = response.get('liqpay_order_id', '')
    description         = response.get('description', '')
    sender_phone        = response.get('sender_phone', '')
    sender_first_name   = response.get('sender_first_name', '')
    sender_last_name    = response.get('sender_last_name', '')
    sender_card_mask2   = response.get('sender_card_mask2', '')
    sender_card_bank    = response.get('sender_card_bank', '')
    sender_card_type    = response.get('sender_card_type', '')
    sender_card_country = response.get('sender_card_country', '')
    ip                  = response.get('ip', '')
    amount              = response.get('amount', '')
    currency            = response.get('currency', '')
    sender_commission   = response.get('sender_commission', '')
    receiver_commission = response.get('receiver_commission', '')
    agent_commission    = response.get('agent_commission', '')
    amount_debit        = response.get('amount_debit', '')
    amount_credit       = response.get('amount_credit', '')
    commission_debit    = response.get('commission_debit', '')
    commission_credit   = response.get('commission_credit', '')
    currency_debit      = response.get('currency_debit', '')
    currency_credit     = response.get('currency_credit', '')
    sender_bonus        = response.get('sender_bonus', '')
    amount_bonus        = response.get('amount_bonus', '')
    mpi_eci             = response.get('mpi_eci', '')
    is_3ds              = response.get('is_3ds', '')
    language            = response.get('language', '')
    create_date         = response.get('create_date', '')
    end_date            = response.get('end_date', '')
    transaction_id      = response.get('transaction_id', '')
    print(response)

    if status == 'failure':
      return redirect('thank_you')
    print("order_id:", order_id)
    order = Order.objects.get(id=order_id)
    # order = Order.objects.get(id=int(order_id)+1000)
    payment = Payment()
    payment.status   = status
    payment.status   = status
    payment.ip       = ip
    payment.amount   = amount
    payment.currency = currency
    payment.order    = order
    payment.sender_phone        = sender_phone
    payment.sender_first_name   = sender_first_name
    payment.sender_last_name    = sender_last_name
    payment.sender_card_mask2   = sender_card_mask2
    payment.sender_card_bank    = sender_card_bank
    payment.sender_card_type    = sender_card_type
    payment.sender_card_country = sender_card_country
    payment.save()
    order.ordered=True
    order.save()
    send_mail(
      subject = 'Замовлення поїздки',
      # message = get_template('contact_message.txt').render({'message':message}),
      message = f'Отримано замовлення поїздки. \n https://www.delfibus.com.ua/admin/order/order/{order.id}/change/',
      from_email = settings.DEFAULT_FROM_EMAIL,
      # recipient_list = settings.DEFAULT_RECIPIENTS,
      recipient_list = [
          'jurgeon018@gmail.com',
          'delfibus0068@gmail.com',
      ],
      fail_silently=False,
      # fail_silently=True,
    )
    # send_user_mail.delay(order.id)
    # non_celery_send_user_mail(order.id)
    send_user_mail(order.id)
    
    return redirect('thank_you')



