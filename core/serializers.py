from rest_framework import serializers
from core.models import *


class TimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Time
    exclude = []


class DirectionSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Direction; 
    exclude = []


class SeatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seat
    exclude = []


class StopSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stop
    exclude = []


class RaceSerializer(serializers.ModelSerializer):
  time = TimeSerializer()
  direction = DirectionSerializer()
  class Meta:
    model = Race
    exclude = []

class SeatInOrderSerializer(serializers.ModelSerializer):
  seat  = SeatSerializer()
  # order = OrderSerializer()
  race  = RaceSerializer()
  class Meta:
    model = SeatInOrder
    exclude = []


# class StopInRaceSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = StopInRace
#     exclude = []


class OrderSerializer(serializers.ModelSerializer):
  seats     = SeatInOrderSerializer(many=True)
  class Meta:
    model   = Order
    exclude = []


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Stop
    exclude = []