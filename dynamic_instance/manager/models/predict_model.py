def predict_with_latest_model(project_id: str, image_path: str):
    print(f"[Instance C] Using latest model for project {project_id}")
    return f"Predicted {image_path} using latest model for {project_id}"
