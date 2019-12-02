from django.shortcuts import (render, get_object_or_404)
from core.utils import (get_sk)
from core.models import (
  Order, Post, Bus, BusComment
)
from django.utils import timezone
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page

def test(request):
  request.session.cycle_key()
  Order.objects.get_or_create(sk=get_sk(request))
  created_time = timezone.now()-timezone.timedelta(minutes=20)
  orders = Order.objects.filter(
    created__lte=created_time,
    ordered=False
  ).delete()
  return render(request, 'test.html', locals())


def order(request):
  request.session.cycle_key()
  created_time = timezone.now()-timezone.timedelta(minutes=20)
  orders = Order.objects.filter(
    created__lte=created_time,
    ordered=False
  ).delete()
  return render(request, 'order.html', locals())


@gzip_page
@cache_page(60*15)
def index(request):
  print(get_sk(request))
  bus_comments = BusComment.objects.all()
  print(bus_comments)
  return render(request, 'index.html', locals())


def park(request):
  buses = Bus.objects.all()
  print(get_sk(request))
  return render(request, 'park.html', locals())


def about_us(request):
  print(get_sk(request))
  return render(request, 'about_us.html', locals())


def contact_us(request):
  return render(request, 'contact_us.html', locals())


def blog(request):
  posts = Post.objects.all()
  return render(request, 'blog.html', locals())


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'post_detail.html', locals())


def thank_you(request):
  return render(request, 'thank_you.html', locals())
