import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': event['detail']['alarmName']},
        UpdateExpression='SET acknowledged = :val',
        ExpressionAttributeValues={':val': 'true'},
    )
