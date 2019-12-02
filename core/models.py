from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.db import models
from datetime import datetime, timedelta
from django.db import models
from django.conf import settings 
from django.utils.translation import ugettext as _
from django.shortcuts import reverse 

# %Y-%m-%d 2006-10-25
# %m/%d/%Y 10/25/2006
# %m/%d/%y 10/25/06
# %H:%M:%S 14:30:59
# %H:%M    14:30


class Time(models.Model):
  time = models.TimeField("Время рейса", blank=True, null=True)
  def __str__(self): return f'{self.time}'
  class Meta: verbose_name = 'Время остановок'; verbose_name_plural = 'Времена остановок'; 


class Direction(models.Model):
  code  = models.CharField(max_length=20, blank=True, null=True, unique=True)
  name  = models.CharField("Направление",max_length=120, blank=True, null=True)
  times = models.ManyToManyField('core.Time', blank=True, null=True)
  stops = models.ManyToManyField('core.Stop', blank=True, null=True)
  # cities_front
  # cities_backward - на случай если маршруты туда-обратно отличаются
  def __str__(self):return f'{self.name}'  
  class Meta: verbose_name = 'Направление'; verbose_name_plural = 'Направления'; 


class Stop(models.Model):
  name = models.CharField("Остановка",max_length=120, blank=True, null=True)
  def __str__(self): return f'{self.name}'
  class Meta: verbose_name = 'Остановка'; verbose_name_plural = 'Остановки'


class Seat(models.Model):
  number = models.CharField("Номер места",max_length=120, blank=True, null=True)
  def __str__(self): return f'{self.number}'
  class Meta: verbose_name = 'Место'; verbose_name_plural = 'Места'; 


class Race(models.Model):
  direction = models.ForeignKey('core.Direction', verbose_name="Направление",on_delete=models.CASCADE, blank=True, null=True)
  time      = models.ForeignKey('core.Time', on_delete=models.CASCADE, verbose_name='Время отправки',blank=True, null=True)
  date      = models.DateField('Дата отправки',blank=True, null=True)
  price     = models.DecimalField('Стоимость',max_digits=10, decimal_places=2, blank=True, null=True, default=10)
  is_full   = models.BooleanField('Полностью заполнен',default=False, blank=True, null=True)
  def __str__(self): return f'{self.direction}, {self.time}, {self.date}, {self.price} UAH'# ,{self.ordered_seats.all()}' 
  class Meta: verbose_name = 'Рейс'; verbose_name_plural = 'Рейсы'


class SeatInOrder(models.Model):
  seat  = models.ForeignKey('core.Seat', verbose_name="Место" ,blank=True, null=True, on_delete=models.CASCADE)
  order = models.ForeignKey('core.Order',verbose_name="Заказ" ,related_name='seats', blank=True, null=True, on_delete=models.CASCADE)
  race  = models.ForeignKey('core.Race', verbose_name="Рейс" ,related_name='seats', blank=True, null=True, on_delete=models.CASCADE)
  def __str__(self): return f'{self.seat}|{self.order.sk}|{self.race}'
  class Meta: verbose_name = 'Место в заказе'; verbose_name_plural = 'Места в заказе'; 


class StopInRace(models.Model):
  stop = models.ForeignKey('core.Stop', verbose_name='Остановка',      on_delete=models.CASCADE, blank=True, null=True)
  time = models.ForeignKey('core.Time', verbose_name='Время остановки',on_delete=models.CASCADE, blank=True, null=True)
  race = models.ForeignKey('core.Race', verbose_name='Рейс',           on_delete=models.CASCADE, blank=True, null=True, related_name='stops', )
  def __str__(self): return f'{self.time.time}|{self.stop.name}'
  class Meta: verbose_name = 'Остановка в рейсе'; verbose_name_plural = 'Остановки в рейсе'


class Order(models.Model):
  full_name = models.CharField(_("Полное имя"),max_length=120, blank=True, null=True)
  phone     = models.CharField("Номер телефона",max_length=120, blank=True, null=True)
  email     = models.EmailField("Емайл",blank=True, null=True)
  departion = models.CharField("Город отправления",max_length=120,blank=True, null=True)
  arrival   = models.CharField("Город прибытия",max_length=120,blank=True, null=True)

  sk        = models.CharField(max_length=120, blank=True, null=True, unique=True)
  race      = models.ForeignKey('core.Race', related_name='orders',verbose_name="Рейс",on_delete=models.CASCADE, blank=True, null=True)

  ordered   = models.BooleanField('завершен', default=False)
  pdf       = models.FileField("Билет",upload_to='pdfs/', null=True, blank=True)
  created   = models.DateTimeField("Создан",auto_now_add=True, auto_now=False, blank=True, null=True)
  updated   = models.DateTimeField("Обновлен",auto_now_add=False, auto_now=True, blank=True, null=True)

  @property
  def price(self):
    price = 0
    for seat in self.seats.all():
      price += seat.race.price
    return price
    # return self.race.price
  def __str__(self): return f'{self.sk}|{self.full_name}|{self.race}'
  class Meta: verbose_name = 'Заказ'; verbose_name_plural = 'Заказы'


class Payment(models.Model):
  status              = models.CharField(max_length=120, blank=True, null=True)
  ip                  = models.CharField(max_length=120, blank=True, null=True)
  amount              = models.CharField(max_length=120, blank=True, null=True)
  currency            = models.CharField(max_length=120, blank=True, null=True)
  order               = models.OneToOneField(Order, verbose_name='Заказ',on_delete=models.CASCADE, blank=True, null=True)
  sender_phone        = models.CharField(max_length=120, blank=True, null=True)
  sender_first_name   = models.CharField(max_length=120, blank=True, null=True)
  sender_last_name    = models.CharField(max_length=120, blank=True, null=True)
  sender_card_mask2   = models.CharField(max_length=120, blank=True, null=True)
  sender_card_bank    = models.CharField(max_length=120, blank=True, null=True)
  sender_card_type    = models.CharField(max_length=120, blank=True, null=True)
  sender_card_country = models.CharField(max_length=120, blank=True, null=True)
  timestamp           = models.DateTimeField(verbose_name='Время',auto_now_add=True, blank=True, null=True)
  def __str__(self):
    return f'{self.order}|{self.amount}|{self.currency}'
  class Meta: verbose_name = 'Оплата'; verbose_name_plural = 'Оплата'; 


class Question(models.Model):
  name     = models.CharField("Имя",max_length=120)
  email    = models.EmailField("Емайл")
  phone    = models.CharField("Телефон",max_length=120)
  question = models.CharField("Тип вопроса",max_length=120)
  message  = models.TextField("Вопрос")
  created  = models.DateTimeField("Создан",auto_now_add=True, auto_now=False, blank=True, null=True)
  updated  = models.DateTimeField("Обновлен",auto_now_add=False, auto_now=True, blank=True, null=True)
  def __str__(self):
    return f'{self.name}|{self.email}|{self.phone}|{self.question}|{self.message}'
  class Meta:
    verbose_name = _("Вопрос")
    verbose_name_plural = _("Вопросы")




class Post(models.Model):
  title   = models.CharField(verbose_name=_("Заголовок"),max_length=120, blank=True, null=True)
  content = HTMLField(verbose_name=_("Контент"), blank=True, null=True)  
  slug    = models.SlugField(verbose_name=_("Ссылка"), blank=True, null=True, max_length=255)
  image   = models.ImageField(verbose_name=_("Картинка"), blank=True, null=True)
  created = models.DateTimeField(verbose_name=_("Создан"), auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(verbose_name=_("Обновлен"), auto_now_add=False, auto_now=True)
  def __str__(self):
    return f'{self.title}'
  class Meta:
    verbose_name = _('Пост')
    verbose_name_plural = _('Посты')
    # app_label = 'pages'
  def get_absolute_url(self):
      return reverse("post_detail", kwargs={"pk": self.pk})
  





class BusGood(models.Model):
  class Meta:
    verbose_name='Удобство автобуса'; verbose_name_plural="Удобства автобуса"; 
  text = models.TextField()
  bus  = models.ForeignKey(to="core.Bus", on_delete=models.CASCADE, related_name="goods", blank=True, null=True)


class BusComment(models.Model):
  class Meta:
    verbose_name='Отзыв к автобусу'; verbose_name_plural="Отзывы к автобусу"; 
  text = models.TextField()
  bus  = models.ForeignKey(to='core.Bus', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)


class Bus(models.Model):
  class Meta:
    verbose_name='Автобус'; verbose_name_plural="Автобусы"; 
  name  = models.CharField(max_length=120)
  photo = models.ImageField()
  def __str__(self):
    return self.name







