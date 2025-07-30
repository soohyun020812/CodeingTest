import boto3, os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def upload_weight(filepath: str):
    bucket = os.getenv("AWS_S3_BUCKET_NAME")
    s3.upload_file(filepath, bucket, filepath)
    print(f"Uploaded {filepath} to S3")
