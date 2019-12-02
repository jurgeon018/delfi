from django.core.management.base import BaseCommand
from item.models import Item, ItemImage, Category, Size
import random
import datetime 
import json 


def generate_items():
  for i in range(1, 10):
    item         = Item()
    item.name    = f'Салфетка № {i}'
    item.name_en = f'Napkin № {i}'
    item.name_uk = f'Серветка № {i}'
    item.name_ru = f'Салфетка № {i}'
    item.description    = f'Описание салфетки № {i}'
    item.description_en = f'Description of napkin № {i}'
    item.description_uk = f'Опис серветки № {i}'
    item.description_ru = f'Описание салфетки № {i}'
    price = round(random.uniform(20, 110), 2)
    item.price = price
    item.discount_price = price - 10
    item.category = Category.objects.get(pk=random.randint(1,6))
    # item.images.add(Image.objects.filter(pk__in=range(1, )))
    # item.size.add(Size.objects.all())
    item.save()
    item.articul = f'{random.randint(1000, 10000)}_{item.pk}'
    # item.articul = random.sample(range(1000, 10000), 1)
    item.save()



class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument(
      'file_name', 
      type=str, 
      help='File, that contains the main item\'s information'
    )

  def handle(self, *args, **kwargs):
    if kwargs.get('file_name', False):
      with open(f"{kwargs['file_name']}") as file:
        data = json.load(file)
    size         = Size()
    
    for cat in data['categories']:
      print(cat)
      category     = Category.objects.get_or_create(
        title=cat['title'],
        slug=cat['slug'],
        image=cat['image']
      )

    for image in data['images']:
      print(image)
      image = ItemImage.objects.get_or_create(
        image=image['image']
      )

    generate_items()

    self.stdout.write(self.style.SUCCESS('Data imported successfully'))
