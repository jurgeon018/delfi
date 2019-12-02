from django.shortcuts import (render, get_object_or_404, reverse, redirect)
from core.utils import get_sk
from django.utils import timezone 
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
from django.utils.translation import ugettext as _
from core.forms import *
from core.models import *
from core.utils import *
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from django.utils.translation import ugettext as _




def create_multiple_races(request):
  form = RaceForm(request.POST or None)
  if request.method == 'POST':
    date_from = request.POST.get('date_from', '')
    date_to   = request.POST.get('date_to', '')
    start     = datetime.strptime(date_from, '%Y-%m-%d')
    end       = datetime.strptime(date_to, '%Y-%m-%d')
    direction = Direction.objects.get(id=request.POST.get('direction', ''))
    time      = Time.objects.get(id=request.POST.get('time', ''))
    dates     = []
    while start <= end:
      dates.append(start.date())
      start += timedelta(days=1)
    for date in dates:
      print(date)
      race, created = Race.objects.get_or_create(
        direction=direction,
        date=date,
        time=time,
      )
      if created:
        race.price=request.POST.get('price','')
        race.save()
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



def test_mail(request):
  # http://localhost:8000/en/admin/order/order/337/change/
  order = Order.objects.get(sk='vbekd254fi79e4c87ofb5gifg8xiw8qy')
  # save_user_order(order)
  # return redirect('index')
  save_user_order(order)
  send_user_mail(order)
  return redirect('test_mail')


def create_bus_comment(request, bus_pk):
  print(request.POST)
  BusComment.objects.create(
    text = request.POST.get('text'),
    bus  = Bus.objects.get(pk=bus_pk),
  )
  send_comment_mail()
  try: return redirect(request.META.get('HTTP_REFERER'))
  except: return redirect('/')


def create_question(request):
  Contact.objects.create(
    name     = request.POST.get('name', ''),
    email    = request.POST.get('email', ''),
    message  = request.POST.get('comment', ''),
    question = request.POST.get('question', ''),
    phone    = request.POST.get('phone', ''),
  )
  send_contact_mail()
  messages.success(request, _('Запитання було добавлений у адмінку'))
  try: return redirect(request.META.get('HTTP_REFERER'))
  except: return redirect('contact_us')




