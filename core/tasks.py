from celery import shared_task, task
from celery.task import periodic_task
from celery.schedules import crontab

from project.celery import app

from datetime import timedelta
from django.utils import timezone
from time import sleep
from weasyprint import HTML, CSS
from core.models import *
from django.http import HttpResponse
from io import BytesIO, StringIO
import string
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import tempfile
import os
from datetime import datetime, date, time, timedelta
from core.models import *



@app.task
def create(request_POST):
  date_from = request_POST.get('date_from', '')
  date_to   = request_POST.get('date_to', '')
  start     = datetime.strptime(date_from, '%Y-%m-%d')
  end       = datetime.strptime(date_to, '%Y-%m-%d')
  direction = Direction.objects.get(id=request_POST.get('direction', ''))
  time      = Time.objects.get(id=request_POST.get('time', ''))
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
      race.price=request_POST.get('price','')
      race.save()
  print('FINISHED!!!')



def non_celery_send_user_mail(order_id):
  order = Order.objects.get(id=order_id)
  seats     = ','.join([seat.seat.number for seat in order.seats.all()])
  context = {
    'order':order,
    'seats':seats,
  }
  template_name = 'ticket.html'
  stylesheets = [
    CSS(os.path.join(settings.BASE_DIR, "static")+'/ticket.css'),
  ]
  pdf_file = HTML(
    string=render_to_string(template_name, context)
  ).write_pdf(stylesheets=stylesheets)
  pdf = HttpResponse(content_type='application/pdf;')
  with tempfile.NamedTemporaryFile(delete=True) as output:
    output.write(pdf_file)
    output.flush()
    output = open(output.name, 'rb')
    pdf.write(output.read())
  filename = f'order_{order.full_name}_{order.pk}.pdf'
  order.pdf.save(
    filename,
    File(BytesIO(pdf.content)),
  )
  email = EmailMessage(
    subject = 'Ваш квиток',
    body = 'Роздрукуйте цей квиток та пред\'явіть його при посадці',
    from_email = settings.DEFAULT_FROM_EMAIL,
    to = [
      order.email
    ],
  )
  email.attach(filename, open(order.pdf.path, 'rb').read(), 'application/pdf')
  email.send(fail_silently=False)

  email = EmailMessage(
    subject = f'Квиток #{order.id}',
    body = f'''Імя: {order.full_name}, 
      \nномер телефону: {order.phone},
      \nмісце прибуття: {order.arrival},
      \nмісце відправки: {order.departion} 
    \nчас відправки: {order.race.time.time}''',
    from_email = settings.DEFAULT_FROM_EMAIL,
    to = settings.DEFAULT_RECIPIENTS
    
  )
  email.attach(filename, open(order.pdf.path, 'rb').read(), 'application/pdf')
  email.send(fail_silently=False)


  # return pdf
  # response = HttpResponse(pdf, content_type='application/pdf')
  # response['Content-Disposition'] = 'attachment; filename="Invoice_12341231.pdf"'
  # return response
  print('EMAIL HAS BEEN SENT')


@app.task
def send_user_mail(order_id):
  non_celery_send_user_mail(order_id)



# @periodic_task(run_every=crontab(), name="create_races_every_night")
# @periodic_task(run_every=timedelta(seconds=10), name="create_races_every_night")
def create_races_every_night():
    directions = Direction.objects.all()
    price = 10
    date = timezone.now()
    for direction in directions:
      times = direction.times.all()
      for time in times:
        Race.objects.create(
          direction=direction,
          time=time,
          date=date,
          price=price,
        )



# @periodic_task(run_every=timedelta(minutes=20), name="delete_orders_older_than_20_minutes")
@periodic_task(run_every=timedelta(seconds=20), name="delete_orders_older_than_20_minutes")
def delete_orders_older_than_20_minutes():
    created_time = timezone.now()-timezone.timedelta(seconds=20)
    # created_time = timezone.now()-timezone.timedelta(minutes=20)
    orders = Order.objects.filter(
        created__lte=created_time,
        ordered=False
    ).delete()
