# incident Escalation Management in AWS

This repository contains the source code and configuration needed to set up an SMS escalation protocol for incident management in Amazon Web Services (AWS). The system is designed to raise an alarm in case of an incident, escalate it if necessary, and prevent unnecessary notifications during a maintenance window.

## Folder Structure

The repository is organized as follows:

- `lambda_functions/` - Contains the Python scripts for each Lambda function.
  - `Check_Maintenance_Window/` - Checks whether a maintenance window is currently active.
  - `Escalation_Level_1/` - Sends a notification to a Slack channel if no maintenance window is active.
  - `Escalation_Level_2/` - Checks if the alarm is still active after 30 minutes, and if it is, sends an SMS notification to the team.
  - `Incident_Response/` - Allows an SRE to acknowledge an alarm and prevent further escalation.
- `state_machine/` - Contains the JSON configuration for the Step Functions state machine.

## Getting Started

To use this system, you need an AWS account and the AWS CLI installed and configured on your machine.

1. Clone this repository: `git clone https://github.com/MarcoCornejo/incident-escalation-management-aws.git`
2. Navigate to each Lambda function directory and deploy the function to your AWS account.
3. Create a state machine in AWS Step Functions using the configuration in `state_machine.json`.
4. Configure your CloudWatch alarms to trigger the state machine whenever their state changes to ALARM.

For more information, see the comments in each script and the accompanying blog post [here](https://medium.com/@MarcoCornejo/keeping-calm-in-the-eye-of-the-storm-establishing-sms-escalation-protocols-for-incident-management-4c5afb3a0628).

# Environment Variables

The following environment variables need to be set in order for the Lambda functions to work correctly:

- `REGION`: The AWS region where your resources are located.
- `ACCOUNT_ID`: Your AWS account ID.
- `SLACK_URL`: The Webhook URL for your Slack workspace.
- `TABLE_NAME`: The name of the DynamoDB table where the alarm and escalation information is stored.

## Feedback

If you have any feedback or run into issues using this system, please open an issue or submit a pull request. Your contributions are welcome!
