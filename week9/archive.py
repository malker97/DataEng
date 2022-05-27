
from google.cloud import storage
import sys
import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

bucket_name = 'breadcrumbs'
# bucket_name = sys.argv[1]
path = sys.argv[1]
file = sys.argv[2]
source_file_name = f'{path}/{file}'
# function source code from https://github.com/googleapis/python-storage/blob/HEAD/samples/snippets/storage_upload_file.py
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
def zipfile(source_file_name):
    original_data = open(source_file_name, 'rb').read()
    compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
    plaintext = compressed_data
    
    key = RSA.import_key(open('public.pem').read())
    cipher = PKCS1_cipher.new(key)
    length = 100
    ciphertexts = []
    for i in range(0, len(plaintext), length):
        ciphertexts.append(base64.b64encode(cipher.encrypt(plaintext[i: i+length])))
    ciphertext = b''.join(ciphertexts)
    compressed_data = ciphertext
    
    f = open(source_file_name, 'wb')
    f.write(compressed_data)
    f.close()

zipfile(source_file_name)
upload_blob(bucket_name, source_file_name, file)