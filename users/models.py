from django.contrib.auth.models import AbstractUser
from django.db import models

'''
Расширьте модель пользователя
1) для регистрации по почте,
2) а также верификации.
'''


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Email",
        unique=True
    )  # email для регистрации и верификации Пользователя

    phone = models.CharField(
        max_length=35,
        verbose_name="Contact phone number",
        blank=True,
        null=True,
    )  # контактный номер телефона Пользователя

    country = models.CharField(
        max_length=55,
        verbose_name="Страна регистрации",
        blank=True,
        null=True,
    )  # страна регистрации Пользователя

    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        blank=True,
        null=True,
    )  # создание Токена

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
