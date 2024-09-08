from users.models import LogActivity
from celery import shared_task


@shared_task
def create_log(*args, **kwargs):
    LogActivity.create(*args, **kwargs)