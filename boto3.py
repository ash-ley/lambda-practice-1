import boto3
import json

def lambda_handler(event, context):
    bucket_name = event['S3Bucket']
    key = event['S3Prefix']
    petName = event['PetName']
    
    s3client = boto3.client('s3')

    list_buckets_resp = s3client.list_buckets()
    for bucket in list_buckets_resp['Buckets']:
        if bucket['Name'] == bucket_name:
            print('Bucket exists')
        else:
            return {
                'statusCode' : 400,
                'body' : "Bucket doesn't exist"
            }
    obj = bucket.Object(key)
    print('Object body: {}'.format(obj.get()['Body'].read()))
    body = obj.get()['Body'].read()
    for name, species, birthYear, favFoods, photo in body['pets']:
        if name == event['name']:
            return {
                'statusCode' : 200,
                'body' : json.dumps(body['favFoods'])
            }