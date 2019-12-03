from django.db import models 
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse


class Post(models.Model):
  title   = models.CharField(verbose_name=_("Заголовок"),max_length=120, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
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
  def get_absolute_url(self):
      return reverse("post_detail", kwargs={"pk": self.pk})
  


class Index(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Главная'; verbose_name_plural="Главная"; 


class About(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'О нас'; verbose_name_plural="О нас"; 


class Contact(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Контакты'; verbose_name_plural="Контакты"; 


class Park(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Автопарк'; verbose_name_plural="Автопарк"; 


class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Блог'; verbose_name_plural="Блог"; 








class BusGood(models.Model):
  class Meta:
    verbose_name='Удобство автобуса'; verbose_name_plural="Удобства автобуса"; 
  text = models.TextField()
  bus  = models.ForeignKey(to="Bus", on_delete=models.CASCADE, related_name="goods", blank=True, null=True)


class BusComment(models.Model):
  class Meta:
    verbose_name='Отзыв к автобусу'; verbose_name_plural="Отзывы к автобусу"; 
  text = models.TextField()
  bus  = models.ForeignKey(to='Bus', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
  moderated = models.BooleanField(default=True)

class Bus(models.Model):
  class Meta:
    verbose_name='Автобус'; verbose_name_plural="Автобусы"; 
  name  = models.CharField(max_length=120)
  photo = models.ImageField()
  def __str__(self):
    return self.name







class Page(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return f"{self.title}"


class Feature(models.Model):
    page = models.ForeignKey(to=Page, verbose_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.TextField()
    def __str__(self):
        return f"{self.page.title}, {self.name}, {self.value}"
    

