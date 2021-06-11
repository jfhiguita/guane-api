"""celery module"""

#standard libraries
import os
from time import sleep

#celery
from celery import Celery
from celery.utils.log import get_task_logger


# init celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@fastapi-rabbit:5672")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://:password123@redis:6379/0")
celery.conf.task_routes = {"worker.celery.test_celery": "test-queue"}
celery.conf.update(task_track_started=True)

# create logger
logger = get_task_logger(__name__)

# celery task
@celery.task
def create_task(name: str):
    sleep(5)
    logger.info(f'zzzzz{name}...Ready!')

    return True