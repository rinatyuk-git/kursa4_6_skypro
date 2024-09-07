from django.core.mail import send_mail

from config import settings
from mailingservice.models import Mailing


def send_mailing(mailing_item: Mailing):
    send_mail(
        f'Новости рассылки от {mailing_item.mailing_name}',
        f'Рассылаем новинки для {mailing_item.message}',
        settings.EMAIL_HOST_USER,
        mailing_item.clients.values_list('client_email', flat=True),
        fail_silently=False,
    )
