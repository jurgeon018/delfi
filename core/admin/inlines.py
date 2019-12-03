from django.contrib import admin 
from core.models import *



class StopInRaceInline(admin.StackedInline):
  model = StopInRace
  exclude = []
  extra = 1


class SeatInOrderInline(admin.StackedInline):
  def has_delete_permission(self, request, obj):
    return False
  def has_add_permission(self, request, obj):
    return False
  
  model = SeatInOrder
  extra = 0
  fields = [
    'seat'
  ]
  readonly_fields = [
    'seat',
  ]


class OrderInline(admin.StackedInline):
  model = Order
  extra = 0
  # readonly_fields = ['direction','race','full_name', 'phone', 'email', 
  # # 'seats', 
  # 'departion', 'arrival', 'pay_type', 'pdf','payment'
  # ]
  exclude = ['sk']


class BusCommentInline(admin.StackedInline):
# class CommentInline(admin.TabularInline):
    model = BusComment
    extra = 3


class RaceInline(admin.StackedInline):
  model = Race
  extra = 0


class PaymentInline(admin.StackedInline):
  model = Payment
  extra = 3
  # readonly_fields = ['direction','race','full_name', 'phone', 'email', 'seat', 'departion', 'arrival', 'pay_type', 'pdf','payment']
  # exclude = ['sk']
