from django.db import models 


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
    






class Index(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 
class About(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 
class Contact(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 
class Park(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 
class Blog(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 
class Order(models.Model):
    class Meta:
        verbose_name = ''; verbose_name=""; 

