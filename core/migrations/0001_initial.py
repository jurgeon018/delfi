from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата отправки')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=10, null=True, verbose_name='Стоимость')),
                ('is_full', models.BooleanField(blank=True, default=False, null=True, verbose_name='Полностью заполнен')),
                ('direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Direction', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=120, null=True, verbose_name='Номер места')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Остановка')),
            ],
            options={
                'verbose_name': 'Остановка',
                'verbose_name_plural': 'Остановки',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время рейса')),
            ],
            options={
                'verbose_name': 'Время остановок',
                'verbose_name_plural': 'Времена остановок',
            },
        ),
        migrations.CreateModel(
            name='StopInRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='core.Race', verbose_name='Рейс')),
                ('stop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Stop', verbose_name='Остановка')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Time', verbose_name='Время остановки')),
            ],
            options={
                'verbose_name': 'Остановка в рейсе',
                'verbose_name_plural': 'Остановки в рейсе',
            },
        ),
        migrations.CreateModel(
            name='SeatInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='order.Order', verbose_name='Заказ')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='core.Race', verbose_name='Рейс')),
                ('seat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Seat', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Место в заказе',
                'verbose_name_plural': 'Места в заказе',
            },
        ),
        migrations.AddField(
            model_name='race',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Time', verbose_name='Время отправки'),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.TextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page', verbose_name='features')),
            ],
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
