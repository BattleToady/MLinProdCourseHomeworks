import os
from minio import Minio
from minio.error import ResponseError

# Initialize MinIO client
minio_client = Minio(
    "10.244.0.20:9000",  # MinIO server endpoint
    access_key=os.environ.get('MINIO_ACCESS_KEY'),
    secret_key=os.environ.get('MINIO_SECRET_KEY'),
    secure=False  
)

def response_error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return 0
        except ResponseError as err:
            print(err)
            return 1
    return wrapper

@response_error_decorator
def create_bucket(bucket_name):
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully")
    else:
        print(f"Bucket '{bucket_name}' already exists")

@response_error_decorator
def upload_file(bucket_name, object_name, file_path):
    minio_client.fput_object(bucket_name, object_name, file_path)
    print(f"File '{object_name}' uploaded to '{bucket_name}' successfully")

@response_error_decorator
def download_file(bucket_name, object_name, local_file_path):
    minio_client.fget_object(bucket_name, object_name, local_file_path)
    print(f"File '{object_name}' downloaded from '{bucket_name}' successfully")

@response_error_decorator
def delete_file(bucket_name, object_name):
    minio_client.remove_object(bucket_name, object_name)
    print(f"File '{object_name}' deleted from '{bucket_name}' successfully")

@response_error_decorator
def delete_bucket(bucket_name):
    minio_client.remove_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully")
