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
                'PartnerName': fake.name(),
                'email': fake.company_email(),
                'address': fake.address(),
                'clientDealValue': str(random.randrange(2500, 1000000, 500))
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
    
    partner_table = boto3.resource('dynamodb').Table('PrometheonPartners')
    add_random_data_to_table(150, partner_table)
    
    # Put specific required values in the table
    partner_table.put_item(
        Item={
            'PartnerName': 'dummy_name_delete_b4_demo',
            'email': 'Dummyemail@emails.com',
            'address': fake.address(),
            'clientDealValue': 'No money, I\'m a dummy value!'
        }
    )
    
    partner_table.put_item(
        Item={
            'PartnerName': 'ProTowTires',
            'email': 'greg@protowtires.com',
            'address': fake.address(),
            'clientDealValue': 'OVER NINE-THOUSAND!!!!'
        }
    )
    
    # Add another 50 random values 
    add_random_data_to_table(50, partner_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, "SUCCESS", {"Status": "SUCCESS"})