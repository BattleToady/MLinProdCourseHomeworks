from minio import Minio
from minio.error import ResponseError

# Initialize MinIO client
minio_client = Minio(
    "10.244.0.20:9000",  # MinIO server endpoint
    access_key="6BECLESS4YMLACAXL0PR",
    secret_key="LnfbL0Ouo4E1OISF3KDGEOX225TBFEe1ujcuEwye",
    secure=False  
)

def create_bucket(bucket_name):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully")
        else:
            print(f"Bucket '{bucket_name}' already exists")
        return 0
    except ResponseError as err:
        print(err)
        return 1

def upload_file(bucket_name, object_name, file_path):
    try:
        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"File '{object_name}' uploaded to '{bucket_name}' successfully")
        return 0
    except ResponseError as err:
        print(err)
        return 1

def download_file(bucket_name, object_name, local_file_path):
    try:
        minio_client.fget_object(bucket_name, object_name, local_file_path)
        print(f"File '{object_name}' downloaded from '{bucket_name}' successfully")
        return 0
    except ResponseError as err:
        print(err)
        return 1

def delete_file(bucket_name, object_name):
    try:
        minio_client.remove_object(bucket_name, object_name)
        print(f"File '{object_name}' deleted from '{bucket_name}' successfully")
        return 0
    except ResponseError as err:
        print(err)
        return 1

def delete_bucket(bucket_name):
    try:
        minio_client.remove_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully")
        return 0
    except ResponseError as err:
        print(err)
        return 1
