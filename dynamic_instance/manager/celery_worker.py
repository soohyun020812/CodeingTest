from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

celery = Celery(
    "instance_tasks",
    broker=os.getenv("REDIS_BROKER_URL"),
    backend=os.getenv("REDIS_BROKER_URL")
)
celery.conf.task_routes = {
    "app.tasks.train_model_task": {"queue": "train"},
    "app.tasks.predict_model_task": {"queue": "predict"},
}
