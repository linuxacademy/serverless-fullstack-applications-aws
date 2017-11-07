#!/usr/bin/env python3

# Creates fake data and pushes it to a dynamoDB Table

import boto3
import cf_response
import random
import time
from faker import Faker

fake = Faker()

def add_testing_data_to_table(num_items, dynamo_table):
    """Seeds DynamoDB table with 'test' values to be deleted"""
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'Artist': 'Stephen James',
                'SongTitle': 'test' + str(counter),
                'AlbumTitle': 'TestyTestersTestyTests',
                'Genre' : 'Classical',
                'Price' : str(random.randrange(0.0,20.0,1)) + random.choice(['.99', '.89']),
                'CriticRating' : random.choice(['1.9','2.3','3.4'])
            }
        )
        time.sleep(0.1)
        counter += 1

# Add some random data to the table 
def handler(event, context):
    print(event)
    print(context)
    
    # Handles the case when this is called during deletion
    if event['RequestType'] == 'Delete':
        cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})
        return 'SUCCESS'
    
    populated_table = boto3.resource('dynamodb').Table('PrometheonMusic')
    
    add_testing_data_to_table(15, populated_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})