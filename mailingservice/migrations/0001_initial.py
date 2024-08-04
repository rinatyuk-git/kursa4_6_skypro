# Generated by Django 5.0.7 on 2024-08-04 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=150, verbose_name='Ф. И. О. Клиента')),
                ('client_email', models.EmailField(max_length=254, unique=True, verbose_name='Контактный email Клиента')),
                ('client_info', models.TextField(blank=True, max_length=2550, null=True, verbose_name='Информация о Клиенте')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['client_name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_name', models.CharField(max_length=150, verbose_name='Тема письма')),
                ('message_body', models.TextField(blank=True, max_length=2550, null=True, verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['message_name'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Тема рассылки')),
                ('started_at', models.DateField(help_text='В формате 2024-08-04', verbose_name='Дата начала рассылки')),
                ('finished_at', models.DateField(blank=True, help_text='В формате 2024-08-04', null=True, verbose_name='Дата окончания рассылки')),
                ('periodic', models.CharField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], default='раз в день', help_text='Выбрать периодичность отправки рассылки', max_length=50, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('создана', 'создана'), ('запущена', 'запущена'), ('завершена', 'завершена')], default='создана', help_text='Узнать статус рассылки', max_length=50, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(help_text='Выбрать клиента', related_name='mailings', to='mailingservice.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(help_text='Выбрать сообщение для рассылки', on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to='mailingservice.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastattempt_at', models.DateTimeField(auto_now_add=True, help_text='В формате 2024-08-04', verbose_name='Дата и время последней попытки')),
                ('status', models.CharField(choices=[('SUCCESS', 'успешно'), ('NOT SUCCESS', 'не успешно')], default='NOT SUCCESS', help_text='Узнать статус попытки', max_length=50, verbose_name='Статус попытки')),
                ('server_answer', models.TextField(blank=True, max_length=2550, null=True, verbose_name='Ответ почтового сервера')),
                ('mailing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailingservice.mailing', verbose_name='Рассылки')),
            ],
        ),
    ]
