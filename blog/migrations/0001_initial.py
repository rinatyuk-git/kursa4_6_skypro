# Generated by Django 5.1 on 2024-09-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(help_text='Введите название блога', max_length=100, verbose_name='Название блога')),
                ('slug', models.CharField(blank=True, max_length=180, null=True, verbose_name='slug')),
                ('blog_info', models.TextField(help_text='Введите информацию о блоге', max_length=1255, verbose_name='Информация о блоге')),
                ('blog_image', models.ImageField(blank=True, help_text='Загрузите изображение в блог', null=True, upload_to='blog/images', verbose_name='Изображение в блоге')),
                ('created_at', models.DateField(auto_now_add=True, help_text='Задайте дату создания блога', verbose_name='Дата создания блога')),
                ('views_count', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
            ],
        ),
    ]
