import boto3
import os
import glob


s3 = boto3.client('s3')

filename = 'list_object.py'
bucket_name="smontes-catch-all"

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, filename)
    print("Object Uploaded")
    
cwd=os.getcwd()