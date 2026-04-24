import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

print("Connected to AWS EC2 successfully")