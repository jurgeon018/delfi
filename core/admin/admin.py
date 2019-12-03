from django.contrib import admin
from django.forms import widgets
from django.db import models 
from django.utils.html import mark_safe
from django.urls import reverse
from .inlines import *
from core.models import *
from core.forms import RaceForm
from django.http import HttpResponse 
# from import_export.admin import ImportExportModelAdmin
import csv 



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = ['Места'] + [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = f'attachement; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            seats = ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
            # row = writer.writerow([getattr(obj, field) for field in field_names[1:]])
            writer.writerow([seats] + [getattr(obj, field) for field in field_names[1:]])
        return response
    export_as_csv.short_description = "Export Selected"



# core 

class DirectionAdmin(admin.ModelAdmin):
  pass


class TimeAdmin(admin.ModelAdmin):
  pass


class StopAdmin(admin.ModelAdmin):
  pass


class SeatAdmin(admin.ModelAdmin):
  pass


class SeatInOrderAdmin(admin.ModelAdmin):
  def get_order(self, obj):
    # option = "change" # "delete | history | change"
    # massiv = []
    # if obj.order:
    #   obj  = obj.order
    #   app   = obj._meta.app_label
    #   model = obj._meta.model_name
    #   url   = f'admin:{app}_{model}_{option}'
    #   args  = (obj.pk,)
    #   href  = reverse(url, args=args)
    #   name  = f'{obj.order.full_name}, {obj.order.phone}, {obj.order.race.direction}'
    #   link = f"<a href={href}>{name}</a>"
    #   return mark_safe(link)
    return f'{obj.order.full_name}, {obj.order.phone}'#, {obj.order.race.direction}'

  get_order.short_description = "Заказ"
  def get_race(self, obj):
    # option = "change" # "delete | history | change"
    # massiv = []
    # if obj.race:
    #   obj  = obj.race
    #   app   = obj._meta.app_label
    #   model = obj._meta.model_name
    #   url   = f'admin:{app}_{model}_{option}'
    #   args  = (obj.pk,)
    #   href  = reverse(url, args=args)
    #   name  = f'{obj.race.direction}, {obj.race.time.time}, {obj.race.date}, {obj.race.price}, {obj.race.is_full}'
    #   link = f"<a href={href}>{name}</a>"
    #   return mark_safe(link)
    f'{obj.race.direction}, {obj.race.time.time}, {obj.race.date}, {obj.race.price}, {obj.race.is_full}'
  get_race.short_description = "Рейс"
  list_display = [
    'seat',
    'get_race',
    'get_order',
  ]
  fields = [
    'seat',
    'get_race',
    'get_order',
  ]
  readonly_fields = [
    'seat',
    'get_race',
    'get_order',
  ]


class RaceAdmin(admin.ModelAdmin):
  # def save_model(self, request, obj, form, change):
  #   date_from = request.POST.get('date_from', '')
  #   date_to   = request.POST.get('date_to', '')
  #   start     = datetime.strptime(date_from, '%Y-%m-%d')
  #   end       = datetime.strptime(date_to, '%Y-%m-%d')
  #   dates = []
  #   while start <= end:
  #     dates.append(start.date())
  #     start += timedelta(days=1)
  #   for date in dates:
  #     print(date)
  #     race, created = Race.objects.get_or_create(
  #       date=date,
  #       time=Time.objects.get(id=request.POST.get('time', '')),
  #     )
  #     if created:
  #       race.direction=Direction.objects.get(id=request.POST.get('direction', ''))
  #       race.price    =request.POST.get('price', '')
  #       race.save()
  #   return super().save_model(request, obj, form, change)
  # actions = []
  actions_on_top = True
  acitons_on_bottom = True 
  actions_selection_couner = True 
  date_hierarchy = 'date' # 'created' | 'updated' |'date'
  empty_value_display = '???'
  change_list_template = 'races_change_list.html'
  # form = RaceForm
  # exclude = [
  # ]
  fields = []
  # fieldsets = []
  # filter_horizontal = ()
  # filter_vertical = ()
  # form # get_form()
  # formfield_overrides = {
  #     models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
  #     # models.DateTimeField: {'widget': widgets.TextInput}
  # }
  inlines = [
    StopInRaceInline, 
    SeatInOrderInline
  ]
  list_display = [
    'id',
    'direction',
    'time',
    'date',
    'price'
  ]
  list_display_links = [
  ]
  list_editable = [
    'price'
  ]
  list_filter = [
    'direction',
    'time',
    'date',
    'price'
  ]
  list_max_show_all = 300
  list_per_page = 20
  list_select_related = False
  ordering = (
    '-id',
  )
  # paginator
  # prepopulated_fields
  # preserve_filters
  # radio_fields
  # autocomplete_fields
  raw_id_fields = [
  ]
  readonly_fields = [
    # "direction",
    # "time",
    # "date",
    # "price",
    "is_full",
  ]
  save_as = False
  save_as_continue = True 
  save_on_top = True
  search_fields = [
    "direction__name",
  ]
  # show_full_result_count
  # sortable_by
  view_on_site = False 


# pages 

class IndexAdmin(admin.ModelAdmin):
  pass 


class AboutAdmin(admin.ModelAdmin):
  pass


class ParkAdmin(admin.ModelAdmin):
  pass


class BlogAdmin(admin.ModelAdmin):
  pass


class ServiceAdmin(admin.ModelAdmin):
  pass


# content 

class BusAdmin(admin.ModelAdmin):
  pass


class BusGoodAdmin(admin.ModelAdmin):
  pass


class BusCommentAdmin(admin.ModelAdmin):
    list_display = [
      'text',
    ]


class PostAdmin(admin.ModelAdmin):
  list_per_page = 4
  search_fields = [
    'title'
  ]
  list_filter = [
    'created',
    'updated',
  ]
  list_display = [
    'title',
    'created',
    'updated',
  ]


# order

class OrderAdmin(admin.ModelAdmin, ExportCsvMixin):
  actions = ['export_as_csv'] 
  def get_race(self, obj):
    option = "change" # "delete | history | change"
    massiv = []
    try:
      obj  = obj.race
      app   = obj._meta.app_label
      model = obj._meta.model_name
      url   = f'admin:{app}_{model}_{option}'
      args  = (obj.pk,)
      href  = reverse(url, args=args)
      name  = obj
      link = f"<a href={href}>{name}</a>"
      return mark_safe(link)
    except: pass
    return obj
  get_race.short_description = "Рейc"
  def get_direction(self, obj):
    option = "change" # "delete | history | change"
    massiv = []
    if obj.direction:
      obj  = obj.direction
      app   = obj._meta.app_label
      model = obj._meta.model_name
      url   = f'admin:{app}_{model}_{option}'
      args  = (obj.pk,)
      href  = reverse(url, args=args)
      name  = obj
      link = f"<a href={href}>{name}</a>"
      return mark_safe(link)
  get_direction.short_description = "Напрямок"
  def seats1(obj):
    # seats_in_order = SeatInOrder.objects.filter(order=obj)
    # if seats_in_order.exists():
    return ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
  def seats2(self, obj):
    # seats_in_order = SeatInOrder.objects.filter(order=obj)
    # if seats_in_order.exists():
    return ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
  seats1.short_description = 'Места'
  seats1.empty_value_display = '????'
  seats2.short_description = 'Места'
  seats2.empty_value_display = '????'
  # actions = []
  actions_on_top = True 
  acitons_on_bottom = True 
  actions_selection_couner = True 
  date_hierarchy = 'created' # 'created' | 'updated' |'date'
  empty_value_display = '???'
  exclude = [
    'sk',
    'race',
    'direction'
  ]
  formfield_overrides = {
      models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
      # models.DateTimeField: {'widget': widgets.TextInput}
  }
  inlines = [
    SeatInOrderInline, 
    PaymentInline
  ]
  list_display = [
    "id",
    # "sk",
    "get_race",
    # seats1,
    'seats2',
    "full_name",
    "phone",
    "email",
    "departion",
    "arrival",
    "ordered",
    "pdf",
    # "direction",
    # "date",
    # "time",
    "created",
    "updated",
  ]
  list_display_links = [
    'id', 
  ]
  list_editable = []
  list_filter = [
    # "direction",
    # "date",
    # "time",
    'departion',
    'arrival',
    'ordered',
    'created',
    'updated',
  ]
  list_max_show_all = 100
  list_per_page = 10
  list_select_related = False
  ordering = (
    '-id',
  )
  # paginator
  # prepopulated_fields
  # preserve_filters
  # radio_fields
  # autocomplete_fields
  # raw_id_fields = [
  #   'race'
  # ]
  readonly_fields = [
    'full_name',
    'phone',
    'email',
    'departion',
    'arrival',
    'get_race',
    # 'get_direction',
    # 'date',
    # 'time',
    'ordered',
    'pdf',
    'created',
    'updated',
  ]
  save_as = False
  save_as_continue = True 
  save_on_top = False
  search_fields = [
    "full_name",
    "phone",
    "email",
  ]
  # show_full_result_count
  # sortable_by
  view_on_site = False 


class PaymentAdmin(admin.ModelAdmin):
  exclude = []
  # list_display_links = ['amt','timestamp','ccy','paycountry']
  # inlines = [OrderInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = [
      'name',
      'email',
      'phone',
      'comment',
      'created',
      'updated',
    ]
    readonly_fields = [
      'name',
      'email',
      'phone',
      'comment',
      'created',
      'updated',
    ]
    search_fields = [
      "name",
      "email",
      "phone",
      "comment",
    ]
    list_filter = [
      'comment',
      'created',
      'updated',
    ]
    list_per_page = 10


class EuropeContactAdmin(admin.ModelAdmin):
  pass


class BusContact(admin.ModelAdmin):
  pass 


