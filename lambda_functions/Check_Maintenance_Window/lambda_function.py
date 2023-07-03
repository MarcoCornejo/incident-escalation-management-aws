import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.get_item(Key={'id': 'maintenance_window'})
    if 'Item' in response:
        return response['Item']['value'] == 'true'
    else:
        return False
