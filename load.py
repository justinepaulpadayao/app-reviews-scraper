import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_to_s3(dataframe):
    s3 = boto3.client('s3')
