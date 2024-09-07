# Generated by Django 5.1 on 2024-09-04 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailingservice', '0003_alter_mailing_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('pk',), 'permissions': [('can_view_mailing_list', 'Can view mailings list'), ('can_view_user_list', 'Can view users list'), ('can_block_user', 'Can block user'), ('can_turnoff_mailing', 'Can turnoff mailing')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
