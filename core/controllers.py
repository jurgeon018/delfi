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
from django.template.loader import get_template, render_to_string 
from django.conf import settings 


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
  bus  = Bus.objects.get(pk=bus_pk)
  text = request.POST.get('text')
  BusComment.objects.create(
    text = text,
    bus  = bus,
  )
  recipient_list = [
    'jurgeon018@gmail.com',
  ]
  if not settings.TEST_LIQPAY:
    recipient_list.append('delfibus0068@gmail.com')
  print(recipient_list)
  send_mail(
    subject = 'Відгук до автобусу',
    message = f"""
    \nПовідомлення: {text}
    \nАвтобус: {bus.name}
    """,
    from_email = settings.DEFAULT_FROM_EMAIL,
    recipient_list = recipient_list, 
    fail_silently=True,
  )
  try: return redirect(request.META.get('HTTP_REFERER'))
  except: return redirect('/')


@csrf_exempt
def create_europe_order(request):
  print(request.POST)
  name    = request.POST.get('name','---')
  phone   = request.POST.get('phone', '---')
  email   = request.POST.get('email', '---')
  comment = request.POST.get('comment', '---')
  peoples = request.POST.get('count_piople', '')
  order   = EuropeContact.objects.create(
    name    = name,
    phone   = phone,
    email   = email,
    comment = comment,
    peoples = int(peoples),
  )
  recipient_list = [
    'jurgeon018@gmail.com'
  ]
  if not settings.TEST_LIQPAY:
    recipient_list.append('delfibus0068@gmail.com')
  print(recipient_list)
  send_mail(
    subject = 'Получено заказ автобуса на Европу.',
    # message = get_template('contact_message.txt').render({'message':message}),
    # message = 'Перейдите по этой ссылке: {CURRENT_DOMEN}/admin/pages/europecontact/',
    message = f"""
    \nІмя:{name}
    \nТелефон:{phone}
    \nПошта:{email}
    \nПовідомлення:{comment}
    """,
    from_email = settings.DEFAULT_FROM_EMAIL,
    recipient_list = recipient_list,
    fail_silently=True,
  )

  return HttpResponse('OK, 200')


@csrf_exempt
def create_bus_order(request):
  print(request.POST)
  name    = request.POST.get('name','')
  phone   = request.POST.get('phone', '')
  email   = request.POST.get('email', '')
  comment = request.POST.get('comment', '---')
  peoples = request.POST.get('count_piople', '')
  order   = BusContact.objects.create(
    name    = name,
    phone   = phone,
    email   = email,
    comment = comment,
    peoples = int(peoples),
  )
  recipient_list = [
    'jurgeon018@gmail.com'
  ]
  if not settings.TEST_LIQPAY:
    recipient_list.append('delfibus0068@gmail.com')
  print(recipient_list)
  send_mail(
    subject = 'Получено заказ Микроавтобуса для поездки по Украине.',
    message = f"""
    \nІмя: {name}
    \nПошта:{email}
    \nТелефон:{phone}
    \nКількість людей:{peoples}
    \nПовідомлення: {comment}
    """,
    from_email = settings.DEFAULT_FROM_EMAIL,
    recipient_list = recipient_list,
    fail_silently=False,
  )
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
  recipient_list = [
    'jurgeon018@gmail.com',
  ]
  if not settings.TEST_LIQPAY:
    recipient_list.append('delfibus0068@gmail.com')
  print(recipient_list)
  send_mail(
    subject = 'Получено контактные данные и вопрос',
    message = f''' 
    \nІмя:{name}
    \nТелефон:{phone}
    \nПошта:{email}
    \nКоментар:{comment}
    ''',
    from_email = settings.DEFAULT_FROM_EMAIL,
    recipient_list = recipient_list,
    fail_silently=False,
  )
  return HttpResponse('OK, 200')


