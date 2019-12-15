from django.shortcuts import (render, get_object_or_404, reverse, redirect)
from core.utils import get_sk
from django.utils import timezone 
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
from django.utils.translation import ugettext as _
from core.forms import *
from core.models import *
from core.utils import *
from core.tasks import *
from django.contrib import messages
from django.utils.translation import ugettext as _
from project.celery import app 




def create_multiple_races(request):
  form = RaceForm(request.POST or None)
  if request.method == 'POST':
    create.delay(request.POST)
  print(request.POST)
  return render(request, 'create_multiple_races.html', locals())


def set_lang(request, lang=None):
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    # lang = request.POST['language']
    url = request.META['HTTP_REFERER'].split('/')
    url[3] = lang
    url = '/'.join(url)
    return redirect(url)




@csrf_exempt
def create_bus_comment(request, bus_pk):
  print(request.POST)
  BusComment.objects.create(
    text = request.POST.get('text'),
    bus  = Bus.objects.get(pk=bus_pk),
  )
  # send_mail(
  #   subject = 'Получено отзыв к автобусу',
  #   # message = get_template('contact_message.txt').render({'message':message}),
  #   message = 'Перейдите по этой ссылке: {CURRENT_DOMEN}/admin/pages/buscomment/',
  #   from_email = settings.DEFAULT_FROM_EMAIL,
  #   recipient_list = [settings.DEFAULT_FROM_EMAIL],
  #   fail_silently=True,
  # )
  try: return redirect(request.META.get('HTTP_REFERER'))
  except: return redirect('/')




@csrf_exempt
def create_europe_order(request):
  print(request.POST)
  name    = request.POST.get('name','')
  phone   = request.POST.get('phone', '')
  email   = request.POST.get('email', '')
  comment = request.POST.get('comment', '')
  peoples = request.POST.get('count_piople', '')
  order   = EuropeContact.objects.create(
    name    = name,
    phone   = phone,
    email   = email,
    comment = comment,
    peoples = int(peoples),
  )
  # send_mail(
  #   subject = 'Получено заказ автобуса на Европу.',
  #   # message = get_template('contact_message.txt').render({'message':message}),
  #   message = 'Перейдите по этой ссылке: {CURRENT_DOMEN}/admin/pages/europecontact/',
  #   from_email = settings.DEFAULT_FROM_EMAIL,
  #   recipient_list = [settings.DEFAULT_FROM_EMAIL],
  #   fail_silently=True,
  # )

  return HttpResponse('OK, 200')



@csrf_exempt
def create_bus_order(request):
  print(request.POST)
  name    = request.POST.get('name','')
  phone   = request.POST.get('phone', '')
  email   = request.POST.get('email', '')
  comment = request.POST.get('comment', '')
  peoples = request.POST.get('count_piople', '')
  order   = BusContact.objects.create(
    name    = name,
    phone   = phone,
    email   = email,
    comment = comment,
    peoples = int(peoples),
  )
  # send_mail(
  #   subject = 'Получено заказ Микроавтобуса для поездки по Украине.',
  #   # message = get_template('contact_message.txt').render({'message':message}),
  #   message = 'Перейдите по этой ссылке: {CURRENT_DOMEN}/admin/pages/orderbus/',
  #   from_email = settings.DEFAULT_FROM_EMAIL,
  #   recipient_list = [settings.DEFAULT_FROM_EMAIL],
  #   fail_silently=True,
  # )
  return HttpResponse('OK, 200')



@csrf_exempt
def create_contact(request):
  print(request.POST)
  name    = request.POST.get('name','')
  phone   = request.POST.get('phone','')
  email   = request.POST.get('email','')
  comment = request.POST.get('comment','')
  contact = Contact.objects.create(
    name=name,
    phone=phone,
    email=email,
    comment=comment,
  )
  # send_mail(
  #   subject = 'Получено контактные данные и вопрос',
  #   # message = get_template('contact_message.txt').render({'message':message}),
  #   message = 'Перейдите по этой ссылке: {CURRENT_DOMEN}/admin/order/contact/',
  #   from_email = settings.DEFAULT_FROM_EMAIL,
  #   recipient_list = [settings.DEFAULT_FROM_EMAIL],#, email],
  #   fail_silently=True,
  # )
  return HttpResponse('OK, 200')





