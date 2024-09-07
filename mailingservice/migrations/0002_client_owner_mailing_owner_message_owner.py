# Generated by Django 5.1 on 2024-09-03 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingservice', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите Создателя клиента', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите Создателя рассылки', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите Создателя сообщения', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
