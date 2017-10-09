#!/usr/bin/env python3

# Creates fake data and pushes it to a dynamoDB Table

import boto3
import cf_response
import random
import time
from faker import Faker

fake = Faker()

def add_random_data_to_table(num_items, dynamo_table):
    """ Seeds DynamoDB table with random data """
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'UserEmail': fake.company_email(),
                'name': fake.name(),
                'address': fake.address(),
                'plan': random.choice(["Platinum", "Gold", "Silver", "Bronze", "Trial"])
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
        cf_response.send(event, context, "SUCCESS", {"Status": "SUCCESS"})
        return 'SUCCESS'
    
    users_table = boto3.resource('dynamodb').Table('Users')
    add_random_data_to_table(150, users_table)
    
    # Put specific required values in the table
    users_table.put_item(
        Item={
            'UserEmail': 'mrdelletteme@freemailemails.com',
            'name': 'Dell Etteme',
            'address': fake.address(),
            'plan': "Test Account"
        }
    )
    
    users_table.put_item(
        Item={
            'UserEmail': 'nedupdatum@emails.com',
            'name': 'Ned Updatum',
            'address': fake.address(),
            'plan': "Trial"
        }
    )
    
    # Add another 50 random values 
    add_random_data_to_table(50, users_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, "SUCCESS", {"Status": "SUCCESS"})