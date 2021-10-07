import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_to_s3(filename,bucket_id,object_name = None):
    s3 = boto3.client('s3')
    s3.upload_file(filename,bucket_id,object_name)
    print(f"Successfuly upload {filename} to S3 bucket {bucket_id}")


