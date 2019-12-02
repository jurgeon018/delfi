from django import forms
from core.models import *
from django.contrib.admin.widgets import AdminDateWidget


CHOICES = (
  ("Основные вопросы","Основные вопросы"),
  ("...","..."),
  ("...","..."),
  ("...","..."),
)



class RaceForm(forms.ModelForm):
  date_from = forms.DateField(required=True, label='Диапазон от', help_text="Вводить дату в формате год-месяц-день(2019-06-23)")#, widget=forms.SelectDateWidget())
  date_to = forms.DateField(required=True, label='Диапазон до', help_text="Вводить дату в формате год-месяц-день(2019-07-15)")#, widget=forms.SelectDateWidget())
  class Meta:
    model = Race
    exclude = ['date', 'is_full']




SEAT_CHOICES = (
  ('1','1'),   ('2','2'),   ('3','3'),
  ('4','4'),   ('5','5'),   ('6','6'),
  ('7','7'),   ('8','8'),   ('9','9'),
  ('10','10'), ('11','11'), ('12','12'), ('13','13'),
  ('14','14'), ('15','15'), ('16','16'), ('17','17'),
  ('18','18'), ('19','19'), ('20','21'), ('21','21'),
)
PAYMENT_CHOICES = (
  ('manager', 'Заказ у менеджера'),
  ('privat24', 'Предоплата на карту Приват24'),
)

