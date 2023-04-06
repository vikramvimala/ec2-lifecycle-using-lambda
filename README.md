# EC2 Instance Lifecycle Management Using AWS Lambda
These two python scripts are used to manage the lifecycle of EC2 instances based on a certain tag. The tag key used to identify the instances is "IncludeInLifecycle". The value of this tag can be set to either "true" or "false".

The `EC2-Start` lambda script is used to start all instances that have the tag "IncludeInLifecycleBeta" with a value of "true" and are currently in a stopped state.

The `EC2-Stop` lambda script is used to stop all instances that have the tag "IncludeInLifecycleBeta" with a value of "true" and are currently in a running state.

## Prerequisites
- AWS account with necessary permissions to manage EC2 instances
- Python 3 installed on the system running the script
- Boto3 Python library installed

## How to Use
1. Clone the repository to your local machine
2. Update the scripts with your desired region
3. Update the scripts with your desired tag name (default is "IncludeInLifecycle")
4. Set the tag value to "true" or "false" for the instances you want to manage
5. Run the scripts using `python3 ec2-start.py` and `python3 ec2-stop.py`

## Notes
- You can run these scripts either locally or using AWS Lambda functions.
- It is recommended to test the scripts on a test environment before running on a production environment.
