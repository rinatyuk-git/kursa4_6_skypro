# Generated by Django 5.1 on 2024-09-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingservice', '0004_alter_mailing_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
