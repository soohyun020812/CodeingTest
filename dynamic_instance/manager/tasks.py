from .celery_worker import celery
from app.manager import Manager

manager = Manager()

@celery.task
def train_model_task(project_id):
    return manager.train(project_id)

@celery.task
def predict_model_task(project_id, image_path):
    return manager.predict(project_id, image_path)
