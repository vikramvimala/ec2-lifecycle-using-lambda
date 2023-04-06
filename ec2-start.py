import os
import boto3


def getEc2Instances(region, tag, state):
    ec2_instances = []
    ec2 = boto3.resource('ec2', region_name=region)
    
    filters = [
        {
        'Name': 'tag:IncludeInLifecycleBeta',
        'Values': [tag]
        },
        {'Name': 'instance-state-name',
            'Values': [state]}
    ]
    
    for instance in ec2.instances.filter(Filters=filters):
        ip = instance.private_ip_address
        state_name = instance.state['Name']
        print("ip:{}, state:{}".format(ip, state_name))
        ec2_instances.append(instance)
        
    return ec2_instances
    
def startEc2Instances(region, tag):
    instances_to_start = getEc2Instances(region, tag, 'stopped')
    instance_state_changed = 0
    print(instances_to_start)
    for instance in instances_to_start:
        print("instance for start:{}".format(instance))
        instance.start()
        instance_state_changed += 1
    return instance_state_changed


def lambda_handler(event, context):
    
    region = os.getenv('REGION', 'eu-central-1')
    tag = os.getenv('IncludeInLifecycleBeta', 'true')
    instance_state_changed = 0
    instance_state_changed = startEc2Instances(region, tag)
    
    return instance_state_changed
