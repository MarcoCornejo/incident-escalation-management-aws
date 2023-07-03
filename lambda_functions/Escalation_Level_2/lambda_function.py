import os
import boto3

sns = boto3.client('sns')
sns_topic_arn = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    response = sns.publish(
        TopicArn=sns_topic_arn,
        Message=f"Alarm: {event['detail']['alarmName']} has triggered and is still active after 30 minutes!",
    )
