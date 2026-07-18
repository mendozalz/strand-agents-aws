import boto3

client = boto3.client("bedrock", region_name="us-east-2")
print(client)