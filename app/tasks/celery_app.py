from celery import Celery
import logging

logging.basicConfig(level=logging.INFO)

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)

celery_app.autodiscover_tasks(["app.tasks"])
