from django.shortcuts import (render, get_object_or_404)
from core.utils import (get_sk)
from core.models import *
from django.utils import timezone
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.shortcuts import (render, get_object_or_404)
from core.utils import (get_sk)
from django.utils import timezone
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.shortcuts import redirect 
from django.conf import settings
from django.http import HttpResponse
from weasyprint import HTML, CSS
from django.template.loader import get_template
import os 





def test_pdf(request):
  # HTML('http://samplewebsite.com/').write_pdf('/localdirectory/test.pdf',
  #   stylesheets=[CSS(string='body { font-size: 10px }')]
  # )
  # CSS(settings.STATIC_ROOT +  'css/main.css')


  # template = "home_page.html"
  template = "ticket.html"
  # static = settings.STATIC_ROOT
  # static = os.path.join(settings.BASE_DIR, "static_root")
  static = os.path.join(settings.BASE_DIR, "static")
  # html_template = get_template(template)
  html_template = get_template(template).render()
  # pdf_file = HTML(string=html_template).write_pdf(stylesheets=[CSS(string='body { font-size: 100px }')])
  pdf_file = HTML(string=html_template).write_pdf(stylesheets=[CSS(static+'/ticket.css')])
  response = HttpResponse(pdf_file, content_type='application/pdf')
  response['Content-Disposition'] = 'filename="home_page.pdf"'
  return response
    


def order(request):
  # return redirect('thank_you')
  request.session.cycle_key()
  created_time = timezone.now()-timezone.timedelta(minutes=2)
  orders = Order.objects.filter(
    created__lte=created_time,
    ordered=False
  ).delete()
  return render(request, 'order.html', locals())


def index(request):
  bus_comments = BusComment.objects.filter(moderated=True)
  # page,_ = Page.objects.get_or_create(name='index')
  # meta_title = page.features.title 
  page = Index.objects.first()
  return render(request, 'index.html', locals())


def park(request):
  buses  = Bus.objects.all()
  # page,_ = Page.objects.get_or_create(name='park')
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


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  # post = Post.objects.get(pk=pk)
  return render(request, 'post_detail.html', locals())


def thank_you(request):
  return render(request, 'thank_you.html', locals())




