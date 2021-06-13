"""celery module"""

#standard libraries
import os

#celery
from celery import Celery
from celery.utils.log import get_task_logger

#send file
from app.send_file import send_f


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
    send_file = send_f()
    logger.info(f'{name}...sending file...')

    return {"message": "Your order has completed!",
            "response_data": send_file}