from django.db import models

from mailingservice.models import NULLABLE


class Blog(models.Model):
    blog_name = models.CharField(
        max_length=100,
        verbose_name="Название блога",
        help_text="Введите название блога",
    )  # заголовок блога
    slug = models.CharField(
        max_length=180,
        verbose_name="slug",
        **NULLABLE,
    )  # slug (реализовать через CharField)
    blog_info = models.TextField(
        max_length=1255,
        verbose_name="Информация о блоге",
        help_text="Введите информацию о блоге",
    )  # содержимое блога
    blog_image = models.ImageField(
        upload_to="blog/images",
        verbose_name="Изображение в блоге",
        help_text="Загрузите изображение в блог",
        **NULLABLE,
    )  # Изображение (превью)
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания блога",
        help_text="Задайте дату создания блога",
    )  # Дата создания (записи в БД)
    views_count = models.IntegerField(
        default=0, verbose_name="Просмотры"
    )  # количество просмотров
    is_published = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )  # признак публикации
