# Generated by Django 2.2.7 on 2019-12-06 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='about',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='index',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='index',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='index',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='index',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='park',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='park',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='park',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='park',
            name='title_uk',
        ),
    ]
