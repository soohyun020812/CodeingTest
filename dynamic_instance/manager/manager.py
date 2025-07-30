from app.models.train_model import train_model
from app.models.predict_model import predict_with_latest_model

class Manager:
    def train(self, project_id: str):
        # 인스턴스 B 생성 및 학습 실행
        result = train_model(project_id)
        return result

    def predict(self, project_id: str, image_path: str):
        # 인스턴스 C 생성 및 최신 모델 추론 실행
        result = predict_with_latest_model(project_id, image_path)
        return result
