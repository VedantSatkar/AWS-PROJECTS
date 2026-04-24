import boto3

iam = boto3.client('iam')

user_name = "devops-user-1"   # use new name to avoid conflict

try:
    response = iam.create_user(
        UserName=user_name
    )
    print("IAM User Created Successfully")

except Exception as e:
    print("Error:", e)