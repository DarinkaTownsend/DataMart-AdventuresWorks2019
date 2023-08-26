import boto3

def download_s3_object(bucket, object, save_as):
    s3_client = boto3.client('s3', 
    aws_access_key_id="AKIAYZN7RIOPN7ZISL7T",
    aws_secret_access_key="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")
    
    s3_client.download_file(bucket, object, save_as)
    

"""
from s3_files import download_s3_object
...
# Guarda el .csv de la tabla de hechos 
bucket = 'adventuretransformado'
object = 'FACT-AdventureWorks_part00000.csv'
save_as = 'FACT-AdventureWorks.csv'

download_s3_object(bucket, object, save_as)
"""