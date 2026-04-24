import boto3

s3 = boto3.client('s3')

bucket_name = "vedant-project-bucket-12345"  # must be globally unique

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("S3 Bucket Created Successfully")