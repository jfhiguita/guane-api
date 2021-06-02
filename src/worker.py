"""celery module"""

#standard libraries
import os
from time import sleep

#celery
from celery import Celery
from celery.utils.log import get_task_logger


# init celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

# create logger
logger = get_task_logger(__name__)

# celery task
@celery.task
def create_task(name: str):
    sleep(5)
    logger.info(f'zzzzz{name}...Ready!')

    return True