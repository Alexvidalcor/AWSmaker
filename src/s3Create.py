import boto3
from botocore.exceptions import ClientError
import logging

def S3_ListBuckets():
    s3 = boto3.resource("s3")
    response = s3.list_buckets()
    return [bucket for bucket in response['Buckets']]

def S3_CreateBucket(bucket_name, region=None):
    print(bucket_name, region)
    try:
        if region is None or region =="us-east-1":
            s3_client = boto3.client('s3')
            s3_clientq.create_bucket(Bucket=bucket_name)
        elif region != "us-east-1":
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def S3_Upload(file_name, bucket, object_name=None):

    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

