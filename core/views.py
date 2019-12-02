from django.shortcuts import (render, get_object_or_404)
from core.utils import (get_sk)
from core.models import *
from pages.models import * 
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


