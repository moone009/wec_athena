from boto3.s3.transfer import S3Transfer
import boto3
import os
from wec_athena import cleanup

class athena_upload:
    def __init__(self, filepath,s3folder,extension,accesskey,secretkey):
        self.filepath = filepath 
        self.s3folder = s3folder 
        self.extension = extension 
        self.accesskey = accesskey 
        self.secretkey = secretkey 
            
    def aws_upload(filepath,s3folder,extension,accesskey,secretkey):
        
        files = cleanup.list_files(filepath,extension)
        for x in range(len(files)):
            
            print(files[x])
            
            source_file = filepath+ '\\'+ files[x]
            
            client = boto3.client('s3', aws_access_key_id=accesskey,aws_secret_access_key=secretkey)
            transfer = S3Transfer(client)
            transfer.upload_file(source_file, 'athenaoregon', s3folder+"/"+files[x])

    
