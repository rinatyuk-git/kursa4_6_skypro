from django.db import models

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):  # Клиент сервиса
    client_name = models.CharField(max_length=150, verbose_name="Ф. И. О. Клиента", )  # Ф. И. О. Клиента
    client_email = models.EmailField(verbose_name="Контактный email Клиента", unique=True, )  # контактный email Клиента
    client_info = models.TextField(max_length=2550, verbose_name="Информация о Клиенте",
                                   **NULLABLE, )  # комментарий по Клиенту

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['client_name']

    def __str__(self):
        return f'{self.client_name}: {self.client_email}'


class Message(models.Model):  # Сообщение для рассылки
    message_name = models.CharField(max_length=150, verbose_name="Тема письма", )  # Тема письма
    message_body = models.TextField(max_length=2550, verbose_name="Тело письма", **NULLABLE, )  # Тело письма

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['message_name']

    def __str__(self):
        return f'{self.message_name}'


class Mailing(models.Model):
    ONCE_DAY = "раз в день"
    ONCE_WEEK = "раз в неделю"
    ONCE_MONTH = "раз в месяц"

    PERIODIC_CHOICES = [
        (ONCE_DAY, "раз в день"),
        (ONCE_WEEK, "раз в неделю"),
        (ONCE_MONTH, "раз в месяц"),
    ]

    CREATED = "создана"
    STARTED = "запущена"
    FINISHED = "завершена"

    STATUS_CHOICES = {
        CREATED: "создана",
        STARTED: "запущена",
        FINISHED: "завершена",
    }

    mailing_name = models.CharField(max_length=150, verbose_name="Тема рассылки", **NULLABLE, )  # Тема рассылки
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name='Сообщение',
        help_text='Выбрать сообщение для рассылки',
        related_name="mailings",
    )
    clients = models.ManyToManyField(
        Client,
        # through="ClientMailing",
        # through_fields=("client", "mailing"),
        verbose_name='Клиенты',
        help_text='Выбрать клиента',
        related_name="mailings",
    )

    started_at = models.DateField(verbose_name='Дата начала рассылки', help_text="В формате 2024-08-04")
    finished_at = models.DateField(verbose_name='Дата окончания рассылки', help_text="В формате 2024-08-04",
                                   **NULLABLE,)
    periodic = models.CharField(
        max_length=50,
        verbose_name='Периодичность',
        help_text='Выбрать периодичность отправки рассылки',
        choices=PERIODIC_CHOICES,
        default=ONCE_DAY,
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Статус рассылки",
        help_text="Узнать статус рассылки",
        choices=STATUS_CHOICES,
        default=CREATED,
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ('pk',)

    def __str__(self):
        return f'{self.mailing_name}'


class Attempt(models.Model):
    STATUS_CHOICES = (
        ('SUCCESS', "успешно"),
        ('NOT SUCCESS', "не успешно"),
    )

    mailing_id = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='Рассылки',
        # related_name="attempts",
    )

    # mailing_name = models.ForeignKey(
    #     Mailing,
    #     on_delete=models.CASCADE,
    #     verbose_name='Рассылки',
    #     # related_name="attempts",
    # )

    # mailing_status = models.ForeignKey(
    #     Mailing,
    #     on_delete=models.CASCADE,
    #     verbose_name='Рассылки',
    #     # related_name="attempts",
    # )

    lastattempt_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время последней попытки',
        help_text="В формате 2024-08-04",
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Статус попытки",
        help_text="Узнать статус попытки",
        choices=STATUS_CHOICES,
        default='NOT SUCCESS',
    )
    server_answer = models.TextField(
        max_length=2550,
        verbose_name="Ответ почтового сервера",
        **NULLABLE,
    )

