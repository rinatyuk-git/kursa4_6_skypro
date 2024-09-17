from datetime import datetime, timedelta

from mailingservice.models import Mailing, Attempt
from mailingservice.services import send_mailing


def check_mailing_status():
    date_now = datetime.now().date()
    for mailing in Mailing.objects.filter(
            status=Mailing.CREATED,
            started_at__lte=date_now,
            finished_at__gt=date_now
    ):
        mailing.status = Mailing.STARTED
        mailing.save()

    # date_next = date_now + 1
    # for mailing in Mailing.objects.filter(
    #         status=Mailing.STARTED,
    #         # finished_at__lt=date_next,
    # ):
    #     # if date_time_next > date_time
    #     mailing.status = Mailing.FINISHED
    #     mailing.save()


def check_send_mailing():
    for mailing in Mailing.objects.filter(status=Mailing.STARTED):
        obj = Attempt.objects.filter(mailing_id=mailing).last()
        if obj is None:
            mailing_time = mailing.time.replace(second=0, microsecond=0)
            now_time = datetime.now().time().replace(second=0, microsecond=0)
            if mailing_time == now_time:
                send_mailing(mailing)
        else:
            periodic = mailing.periodic
            obj_time = obj.lastattempt_at

            if periodic == Mailing.ONCE_DAY:
                obj_time += timedelta(days=1)
            elif periodic == Mailing.ONCE_WEEK:
                obj_time += timedelta(days=7)
            elif periodic == Mailing.ONCE_MONTH:
                obj_time += timedelta(days=30)
            obj_time = obj_time.replace(second=0, microsecond=0)
            now_time = datetime.now().replace(second=0, microsecond=0)
            if obj_time == now_time:
                send_mailing(mailing)


def once_week_mailing():
    pass


def once_month_mailing():
    pass
