import sys
from google.cloud import storage
# function source code from https://github.com/googleapis/python-storage/blob/HEAD/samples/snippets/storage_upload_file.py

def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created")
create_bucket(bucket_name=sys.argv[1])