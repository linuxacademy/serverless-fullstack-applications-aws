#!/usr/bin/env python3

# Creates fake data and pushes it to a dynamoDB Table

import boto3
import time
from faker import Faker

fake = Faker()
dynamodb_client = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')

# Create Table
dynamodb_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
    ],
    TableName='PrometheonPartners',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 15,
        'WriteCapacityUnits': 15
    },
)

# Wait for table to be created (In ACTIVE state)
def check_status():
    return 'ACTIVE' == dynamodb_client.describe_table(TableName='PrometheonPartners')['Table']['TableStatus']

while check_status() != True:
    time.sleep(5)

# Create a resource and then start populating data
table = dynamodb_resource.Table('PrometheonPartners')

counter = 0
while counter < 300:
    response = table.put_item(
        Item={
            'name': fake.name(),
            'email': fake.company_email(),
            'address': fake.address()
        }
    )
    print(response)
    time.sleep(2)
    counter += 1


