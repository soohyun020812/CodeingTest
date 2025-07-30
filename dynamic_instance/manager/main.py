from fastapi import FastAPI, UploadFile
from app.tasks import train_model_task, predict_model_task
import redis

app = FastAPI()

@app.post("/train")
async def train(project_id: str):
    task = train_model_task.delay(project_id)
    return {"message": "Training started", "task_id": task.id}

@app.post("/predict")
async def predict(project_id: str, image: UploadFile):
    task = predict_model_task.delay(project_id, image.filename)
    return {"message": "Prediction started", "task_id": task.id}

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
