from app.utils.s3 import upload_weight

def train_model(project_id: str):
    print(f"[Instance B] Training model for project {project_id}")
    weight_path = f"{project_id}_weights.pt"
    upload_weight(weight_path)
    return f"Training completed. Weights uploaded to S3: {weight_path}"
