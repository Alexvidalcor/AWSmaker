import boto3
from botocore.exceptions import ClientError
import logging

def S3_GetName():
    s3 = boto3.resource("s3")
    return [bucket for bucket in s3.buckets.all()]

def S3_CreateBucket(bucket_name, region=None):
    print(bucket_name, region)
    try:
        if region is None or region =="us-east-1":
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        elif region != "us-east-1":
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

