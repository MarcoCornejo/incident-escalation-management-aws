import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

def lambda_handler(event, context):
    try:
        response = client.chat_postMessage(
            channel=os.environ['SLACK_CHANNEL'],
            text=f"Alarm: {event['detail']['alarmName']} has triggered!"
        )
    except SlackApiError as e:
        assert e.response["error"]
