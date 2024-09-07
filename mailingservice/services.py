import smtplib
from datetime import datetime

from django.core.mail import send_mail

from config import settings
from mailingservice.models import Mailing, Attempt


def send_mailing(mailing_item: Mailing):
    now = datetime.utcnow()
    try:
        send_mail(
            f'Новости рассылки от {mailing_item.mailing_name}',
            f'Рассылаем новинки для {mailing_item.message}',
            settings.EMAIL_HOST_USER,
            mailing_item.clients.values_list('client_email', flat=True),
            fail_silently=False,
        )
        obj = Attempt(
            mailing_id=mailing_item,
            lastattempt_at=now,
            status='SUCCESS',
            # server_answer=f'{e}'
        )
        obj.save()
    except smtplib.SMTPException as e:
        obj = Attempt(
            mailing_id=mailing_item,
            lastattempt_at=now,
            status='NOT SUCCESS',
            server_answer=f'{e}')
        obj.save()
