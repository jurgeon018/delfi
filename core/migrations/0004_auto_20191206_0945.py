# Generated by Django 2.2.7 on 2019-12-06 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_stopinrace'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
