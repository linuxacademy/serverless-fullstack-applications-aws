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
                'AffiliateEmail': fake.free_email(),
                'blog': fake.url(),
                'totalReferrals': str(random.choice([random.randrange(0, 45), random.randrange(0, 15)])),
                'standing': random.choice(['active', 'trial'])
            }
        )
        time.sleep(0.1)
        counter += 1



def add_testing_data_to_table(num_items, dynamo_table):
    """Seeds DynamoDB table with 'test' values to be deleted"""
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'AffiliateEmail': 'test_affiliate' + str(counter + 1) + '@affiliatetests.com',
                'blog': fake.url(),
                'totalReferrals': '0',
                'standing': 'test'
            }
        )
        time.sleep(0.1)
        counter += 1

def add_affiliate_trial_data_to_table(num_items, dynamo_table):
    """Seeds DynamoDB table with values to be updated"""
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'AffiliateEmail': 'affiliate' + str(counter + 1) + '@sarahspenceraffilates.com',
                'blog': 'sarahspenceraffilates.com',
                'totalReferrals': random.randrange(3,27),
                'standing': 'trial'
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
    
    affiliate_table = boto3.resource('dynamodb').Table('PrometheonAffiliates')
    
    add_random_data_to_table(50, affiliate_table)
    add_testing_data_to_table(15, affiliate_table)
    add_affiliate_trial_data_to_table(10, affiliate_table)
    add_random_data_to_table(25, affiliate_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})