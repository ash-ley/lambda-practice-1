import boto3
import json

def lambda_handler(event, context):
    bucket_name = event['S3Bucket']
    key = event['S3Prefix']
    petName = event['PetName']
    
    s3client = boto3.client('s3')
    
    list_buckets_resp = s3client.list_buckets()
    for bucket in list_buckets_resp['Buckets']:
        print(bucket['Name'] + " " + bucket_name)
        if bucket['Name'] == bucket_name:
            print('Bucket exists')
            s3resource = boto3.resource('s3')
            myBucket = s3resource.Bucket(bucket_name)
            obj = myBucket.Object(key)
            body = format(obj.get()['Body'].read().decode('utf-8'))
            jsonContent = json.loads(body)
            
            for pet in jsonContent['pets']:
                if petName == pet['name']:
                    return {
                        'statusCode' : 200,
                        'body' : json.dumps(pet['favFoods'])
                    }
        else:
            return {
                'statusCode' : 404,
                'body' : "Bucket doesn't exist"
            }