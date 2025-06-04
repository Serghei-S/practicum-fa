from celery import Celery
from .config import REDIS_URL

app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks.tasks"]
)

app.autodiscover_tasks(["app.tasks"])