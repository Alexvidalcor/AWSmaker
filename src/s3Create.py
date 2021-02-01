import boto3
from botocore.exceptions import ClientError


def S3_ListBuckets():
    s3 = boto3.resource("s3")
    return [(pos, bucket.name) for pos, bucket in enumerate(s3.buckets.all())]

def S3_CreateBucket(bucket_name, region=""):
    if region == "":
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=region)
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration={'LocationConstraint': region})
    return True


def S3_Upload(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    data = open('test.jpg', 'rb')
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
    return True

