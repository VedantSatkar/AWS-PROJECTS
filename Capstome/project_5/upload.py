import boto3

s3 = boto3.client('s3')

s3.upload_file(
    "index.html",
    "vedant-static-site",
    "index.html",
    ExtraArgs={
        "ContentType": "text/html",
        "ACL": "public-read"
    }
)

print("✅ Uploaded correctly with content-type!")