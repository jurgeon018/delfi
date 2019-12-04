from time import time 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from core.utils import *
from core.models import *
from core.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.core.serializers import serialize
from django.utils.translation import ugettext as _
from time import time
from core.liqpay import LiqPay
from django.conf import settings 
from django.db import connection 



@csrf_exempt
def set_params(request):
  print(request.POST)
  for k,v in request.session.items():
    print(k, v)
  response = {}
  direction = request.POST.get('direction', None)
  date      = request.POST.get('date', None)
  time      = request.POST.get('time', None)
  if direction:
    direction = Direction.objects.get(code=direction)
    request.session['order_direction_id'] = direction.id
    response['order_direction'] = direction.name

  if date:
    full_date = date.strip() # 2019-11-14
    request.session['order_date'] = full_date
    response['order_date'] = full_date

  if time:
    time = Time.objects.get(time=str(time))
    request.session['order_time_id'] = time.id
    response['order_time'] = time.time

  directions = DirectionSerializer(Direction.objects.all(), many=True)
  direction  = Direction.objects.get(id=request.session.get('order_direction_id', ''))

  response['directions'] = directions.data # list(Direction.objects.values_list('name', flat=True))
  response['cities']     = list(direction.stops.values_list('name', flat=True))

  races = Race.objects.filter(
    direction__id=request.session.get('order_direction_id', '')
  )
  response['dates'] = list(races.values_list('date', flat=True).distinct())

  try:
    races = Race.objects.filter(
      direction__id=request.session.get('order_direction_id', ''),
      date=request.session.get('order_date', ''),
    )
    response['times'] = list(Time.objects.filter(race__in=races).values_list('time', flat=True))
  except:
    print("Обрабатываем ошибку date must be in format yyyy-mm-dd not ''")

  try:
    races = Race.objects.filter(
      direction__id=request.session.get('order_direction_id', ''),
      date=request.session.get('order_date', ''),
      time__id=request.session.get('order_time_id', ''),
    )
    if races.exists():
      race = races.first()
      # seats = {}
      response['seats_numbers'] = list(Seat.objects.values_list('number', flat=True))
      seats_in_order = []
      seats_in_order_qs = SeatInOrder.objects.filter(race=race)
      for seat_in_order in seats_in_order_qs:
        if seat_in_order.order:
          order_sk = seat_in_order.order.sk
        else:
          order_sk = None
        seats_in_order.append({
          'number':seat_in_order.seat.number,
          'order_sk': order_sk
        })
        response['seats_in_order'] = seats_in_order


    # order = Order.objects.get(sk=get_sk(request), ordered=False)
    order, _ = Order.objects.get_or_create(sk=get_sk(request), ordered=False)
    response['order_sk'] = order.sk
    response['order_seats'] = [seat.seat.number for seat in order.seats.all()]
  except:
    print('time error')
  for k, v in response.items():
    print(k)
    print(v)
  return JsonResponse(response)


@csrf_exempt
def get_seats(request):
  response = {}

  race = Race.objects.filter(
    direction__id=request.session['order_direction_id'],
    date=request.session['order_date'],
    time__id=request.session['order_time_id'],
  )
  if race.exists():
    race = race.first()
    seats = {}
    # print(Seat.objects.values_list('number', flat=True))
    # response['seats_numbers'] = [seat.number for seat in Seat.objects.all()]
    response['seats_numbers'] = list(Seat.objects.values_list('number', flat=True))
    seats_in_order = []
    seats_in_order_qs = SeatInOrder.objects.filter(race=race)
    for seat_in_order in seats_in_order_qs:
      if seat_in_order.order:
        order_sk = seat_in_order.order.sk
      else:
        order_sk = None
      seats_in_order.append({
        'number':seat_in_order.seat.number,
        'order_sk': order_sk
      })
      response['seats_in_order'] = seats_in_order

  sk = get_sk(request)
  print(sk)
  order = Order.objects.get(sk=sk, ordered=False)
  response['order_sk'] = order.sk
  response['order_seats'] = [seat.seat.number for seat in order.seats.all()]

  return JsonResponse(response)


@csrf_exempt
def create_order(request):
  print(request.POST)
  full_name = request.POST.get('full_name','')
  phone     = request.POST.get('phone','')
  email     = request.POST.get('email','')
  payment   = request.POST.get('payment','')
  departion = request.POST.get('departion','')
  arrival   = request.POST.get('arrival','')
  sk = get_sk(request)
  order     = Order.objects.get(sk=sk, ordered=False )
  order.full_name = full_name
  order.phone     = phone
  order.email     = email
  order.departion = departion
  order.arrival   = arrival
  order.save()
  # set_seats(request)
  seats = dict(request.POST).get('seats')
  # import pdb; pdb.set_trace();
  race = Race.objects.filter(
    direction__id = request.session.get('order_direction_id', ''),
    time__id      = request.session.get('order_time_id', ''),
    date          = request.session.get('order_date', ''),
  )
  if race.exists():
    race = race.first()
    order = Order.objects.get(sk=get_sk(request), ordered=False)
    order.race = race
    order.save()
  if seats:
    print('yes')
    for seat in seats:
      print('seat:', seat)
      ordered_seat_number = Seat.objects.get(number=seat)
      seat_in_order = SeatInOrder.objects.filter(seat=ordered_seat_number, race=race)
      if seat_in_order.exists():
        print('seat is ordered')
        return HttpResponse('seat is ordered')
      else:
        SeatInOrder.objects.create(
          seat=ordered_seat_number,
          order=order,
          race=race
        )
  order.save()
  # send_user_mail(order)
  # send_order_mail()
# для тестовых целей, чтобы каждый раз не вводить номер карты
  order.ordered = True 
  order.save()
  return redirect('thank_you')
#
  return redirect('pay')



