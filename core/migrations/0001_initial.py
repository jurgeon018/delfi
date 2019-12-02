 

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Полное имя')),
                ('phone', models.CharField(blank=True, max_length=120, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Емайл')),
                ('departion', models.CharField(blank=True, max_length=120, null=True, verbose_name='Город отправления')),
                ('arrival', models.CharField(blank=True, max_length=120, null=True, verbose_name='Город прибытия')),
                ('sk', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('ordered', models.BooleanField(default=False, verbose_name='завершен')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/', verbose_name='Билет')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Емайл')),
                ('phone', models.CharField(max_length=120, verbose_name='Телефон')),
                ('question', models.CharField(max_length=120, verbose_name='Тип вопроса')),
                ('message', models.TextField(verbose_name='Вопрос')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
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
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='core.Order', verbose_name='Заказ')),
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
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=120, null=True)),
                ('ip', models.CharField(blank=True, max_length=120, null=True)),
                ('amount', models.CharField(blank=True, max_length=120, null=True)),
                ('currency', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_phone', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_card_mask2', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_card_bank', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_card_type', models.CharField(blank=True, max_length=120, null=True)),
                ('sender_card_country', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплата',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.Race', verbose_name='Рейс'),
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
