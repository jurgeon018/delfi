from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.contrib import messages
from django.template import Context
from django.http import HttpResponse
from io import BytesIO, StringIO
import random 
import string
from django.core.mail import send_mail
from django.conf import settings
# from weasyprint import HTML
from django.core.files import File
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import tempfile
from django.urls import path


CURRENT_DOMEN = settings.CURRENT_DOMEN


def send_user_mail(order):
  print('send_user_mail')
  save_user_order(order)
  email = EmailMessage(
    subject = 'Ваш квиток',
    body = 'Роздрукуйте, будь-ласка, цей квиток, інакше не пустимо вас у автобус',
    from_email = settings.DEFAULT_FROM_EMAIL,
    to = [order.email],
  )
  email.attach('ticket.pdf', open(order.pdf.path, 'rb').read(), 'application/pdf')
  email.send(fail_silently=False)


def save_user_order(order):
  print('save_user_order')
  try:
    payment = order.payment
  except:
    payment = None
  pdf = render_to_pdf('ticket.html', {
    'full_name': "ФИО: "+order.full_name, 
    'phone':"Номер Телефона: "+order.phone,
    'email':"Емаил: "+order.email,
    'seat':"Посадочные места: "+','.join([seat.seat.number for seat in order.seats.all()]),
    'arrival': 'Город прибытия: '+order.arrival,
    'departion':"Город отправления: "+order.departion,
    'payment':f"Оплата: {payment}",
  })
  filename = f'order_{order.full_name}_{order.pk}.pdf'
  order.pdf.save(filename, File(BytesIO(pdf.content)))
  response = HttpResponse(pdf, content_type='application/pdf')
  # строка ниже позволяет скачивать файл
  # response['Content-Disposition'] = 'attachment;'# filename="Invoice_12341231.pdf"'
  return response


def render_to_pdf(template_name, context={}):
  html_string = render_to_string('ticket.html', {'people': 'people'})
  html_string = render_to_string(template_name, context)
  html = HTML(string=html_string)
  result = html.write_pdf()
  response = HttpResponse(content_type='application/pdf;')
  response['Content-Disposition'] = 'inline; filename=list_people.pdf'
  # response['Content-Transfer-Encoding'] = 'binary'
  with tempfile.NamedTemporaryFile(delete=True) as output:
    output.write(result)
    output.flush()
    output = open(output.name, 'rb')
    response.write(output.read())
  return response





def get_sk(request):
  sk = request.session.session_key
  if not sk: request.session.cycle_key()
  return sk 







def send_order_mail():
  send_mail(
    subject = 'Order form Received',
    # message = get_template('contact_message.txt').render({'message':message}),
    message = 'Було отримано замовлення. Перейдіть по цій ссилці: {CURRENT_DOMEN}/admin/order/order/',
    from_email = settings.DEFAULT_FROM_EMAIL,
    recipient_list = [settings.DEFAULT_FROM_EMAIL],#, email],
    fail_silently=True,
  )