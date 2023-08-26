import boto3

def download_s3_object(bucket, object, save_as):
    s3_client = boto3.client('s3', 
    aws_access_key_id="AKIAYZN7RIOPN7ZISL7T",
    aws_secret_access_key="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")
    
    s3_client.download_file(bucket, object, save_as)
    