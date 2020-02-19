from django.shortcuts import (render, get_object_or_404)
from core.models import *
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.shortcuts import (render, get_object_or_404)
from core.utils import *
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import os



def test_mail(request):
  pdf = send_user_mail.delay(order_id=Order.objects.all().first().id)
  # response = HttpResponse(pdf, content_type='application/pdf')
  # response['Content-Disposition'] = 'attachment; filename="Invoice_12341231.pdf"'
  # return response


def order(request):
  request.session.cycle_key()
  page = Service.objects.first()
  return render(request, 'order.html', locals())


def index(request):
  bus_comments = BusComment.objects.filter(moderated=False)
  print(bus_comments)
  page = Index.objects.first()
  return render(request, 'index.html', locals())


def park(request):
  buses  = Bus.objects.all()
  page   = Park.objects.first()
  return render(request, 'park.html', locals())


def about_us(request):
  page = About.objects.first()
  return render(request, 'about_us.html', locals())


def contact_us(request):
  page = ContactUs.objects.first()
  return render(request, 'contact_us.html', locals())


def blog(request):
  posts = Post.objects.all()
  page = Blog.objects.first()
  return render(request, 'blog.html', locals())


def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  page = post 
  return render(request, 'post_detail.html', locals())


def thank_you(request):
  return render(request, 'thank_you.html', locals())


def page404(request):
  return render(request, '404.html', locals())


def oferta(request):
  from django.conf import settings 
  from django.http import FileResponse
  path = os.path.join(settings.STATICFILES_DIRS[0], 'pdf', 'oferta.pdf')
  response = FileResponse(open(path, 'rb'), content_type='application/pdf')
  return response


