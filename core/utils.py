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
from django.core.files import File
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import tempfile
from django.urls import path
# from weasyprint import HTML, CSS
from core.models import Order
import os


def send_user_mail(order):
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
    body = 'Роздрукуйте, будь-ласка, цей квиток, інакше не пустимо вас у автобус',
    from_email = settings.DEFAULT_FROM_EMAIL,
    to = [order.email],
    # to = ['jurgeon018@gmail.com',]
  )
  email.attach(filename, open(order.pdf.path, 'rb').read(), 'application/pdf')
  email.send(fail_silently=False)
  return pdf
  # response = HttpResponse(pdf, content_type='application/pdf')
  # response['Content-Disposition'] = 'attachment; filename="Invoice_12341231.pdf"'
  # return response


def get_sk(request):
  sk = request.session.session_key
  if not sk: request.session.cycle_key()
  return sk
