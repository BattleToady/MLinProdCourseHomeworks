import pytest
from data import minio_client

bucket_name = "example-bucket"
file_to_upload = "example.txt"
local_download_path = "/path/to/download/example.txt"

assert minio_client.create_bucket(bucket_name) == 0
assert minio_client.upload_file(bucket_name, file_to_upload, "/path/to/upload/example.txt") == 0
assert minio_client.download_file(bucket_name, file_to_upload, local_download_path) == 0
assert minio_client.delete_file(bucket_name, file_to_upload) == 0
assert minio_client.delete_bucket(bucket_name) == 0