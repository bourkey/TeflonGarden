# author: @bourkey
# License: 
# Code to create short lived snapshots for use via API
# 
# 
import boto3
import os

region = os.environ.get['AWS_REGION']
snapshotTag = os.environ.get['SNAPSHOTTAG']
snapshotTagValue = os.environ.get['SNAPSHOTTAGVALUE']
tcsProjectID = 
tcs

regionList = ["us-east-1",
            "us-west-1",
            "us-east-2",
            "us-west-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-south-1",
            "eu-central-1",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "sa-east-1"
            ]

def lambda_handler(event, context):
    #Check region against supported list
    if not (region in regionList):
        exit(1)
    #enumerate instances in regions
    ec2client = boto3.client('ec2')
    ec2 = boto3.resource('ec2')
    ec2InstancesForAssessment = 
    instances = ec2.instances.filter(
        Filters=[{'Name': "tag:" + snapshotTag, 'Values': ['' + snapshotTagValue]}}])
    if not instances:
        exit(1)
    for instance in instances:
        ec2InstancesForAssessment.append(instance.id)
    # Do something with AWS


    # Do something with T.cs 

    # Rubbish Collection


