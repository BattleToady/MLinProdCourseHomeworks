import os
import pytest
from data import minio_client

bucket_name = "example-bucket"
file_to_upload = "example.txt"
local_download_path = "/path/to/download/example.txt"

def test_minio_client_create_bucket():
	assert minio_client.create_bucket(bucket_name) == 0

def test_minio_client_upload_file():
	assert minio_client.upload_file(bucket_name, file_to_upload, "/path/to/upload/example.txt") == 0

def test_minio_client_download_file():
	assert minio_client.download_file(bucket_name, file_to_upload, local_download_path) == 0
	os.remove(local_download_path)

def test_minio_client_delete_file():
	assert minio_client.delete_file(bucket_name, file_to_upload) == 0

def test_minio_client_delete_bucket():
	assert minio_client.delete_bucket(bucket_name) == 0