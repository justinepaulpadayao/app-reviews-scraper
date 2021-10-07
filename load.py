import logging
import boto3
from botocore.exceptions import ClientError
import os

<<<<<<< Updated upstream
def upload_to_s3(dataframe):
    s3 = boto3.client('s3')
=======
from botocore.retries import bucket

# TODO create a function to remove the header of the csv file to be uploaded to S3
# TODO create a function to upload the file to S3


def upload_to_s3(filename,bucket_id,object_name = None):
    s3 = boto3.client('s3')
    s3.upload_file(filename,bucket_id,object_name)
    print(f"Successfuly upload {filename} to S3 bucket {bucket_id} ")
>>>>>>> Stashed changes
