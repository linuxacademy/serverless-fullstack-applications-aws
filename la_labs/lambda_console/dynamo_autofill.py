#!/usr/bin/env python3

# Creates fake data and pushes it to a dynamoDB Table

import boto3
import cf_response
import time
import json

dynamo_db = boto3.client('dynamodb')

def handler(event, context):
    print(event)
    print(context)
    
    # Handles the case when this is called during deletion
    if event['RequestType'] == 'Delete':
        cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})
        return 'SUCCESS'
    
    f = open('musicData.json')
    request_items = json.loads(f.read())

    music_table = boto3.resource('dynamodb').Table('PrometheonMusic')
    for item in request_items:
        music_table.put_item(Item=item)
        time.sleep(.21)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})