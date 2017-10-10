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
                'ClientEmail': fake.free_email(),
                'accountType': random.choice(['active', 'trial', 'pending_renewal'])
            }
        )
        time.sleep(0.1)
        counter += 1


def add_values_to_update_into_table(num_items, dynamo_table):
    """Seeds DynamoDB table with values to be updated from trial --> test"""
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'ClientEmail': 'make_me_a_test_account' + str(counter + 1) + '@testaccounts.com',
                'accountType': 'trial'
            }
        )
        time.sleep(0.1)
        counter += 1


def add_values_to_delete_into_table(num_items, dynamo_table):
    """Seeds DynamoDB table with 'test' values to be deleted"""
    counter = 0
    while counter < num_items:
        dynamo_table.put_item(
            Item={
                'ClientEmail': 'please_delete_me' + str(counter + 1) + '@delete_these_accounts.com',
                'accountType': 'active'
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
    
    clients_table = boto3.resource('dynamodb').Table('ClientsTable')
    
    add_random_data_to_table(50, clients_table)
    add_values_to_delete_into_table(15, clients_table)
    add_values_to_update_into_table(10, clients_table)
    add_random_data_to_table(35, clients_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})