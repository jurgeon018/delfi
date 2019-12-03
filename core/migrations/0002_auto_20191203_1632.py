# Generated by Django 2.2.7 on 2019-12-03 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatinorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='order.Order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='seatinorder',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='core.Race', verbose_name='Рейс'),
        ),
        migrations.AddField(
            model_name='seatinorder',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Seat', verbose_name='Место'),
        ),
        migrations.AddField(
            model_name='race',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Direction', verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='race',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Time', verbose_name='Время отправки'),
        ),
        migrations.AddField(
            model_name='feature',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page', verbose_name='features'),
        ),
        migrations.AddField(
            model_name='direction',
            name='stops',
            field=models.ManyToManyField(blank=True, null=True, to='core.Stop'),
        ),
        migrations.AddField(
            model_name='direction',
            name='times',
            field=models.ManyToManyField(blank=True, null=True, to='core.Time'),
        ),
    ]
