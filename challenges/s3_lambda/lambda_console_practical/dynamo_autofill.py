#!/usr/bin/env python3

# Creates fake data and pushes it to a dynamoDB Table

import boto3
import cf_response
import random
import time
from faker import Faker

fake = Faker()

# Create random 85 companies
def create_random_companies_and_ids():
    companies = []
    while len(companies) < 85:
        companies.append(fake.company())
        # keep unique values only
        companies = set(companies)
        companies = list(companies)

    companies_and_ids = []

    for company in companies:
        company_id = company.lower().replace(' ','').replace(',','').replace('-','')
        companies_and_ids.append([company, company_id])

    return companies_and_ids

COMPANIES_AND_IDS = create_random_companies_and_ids()

def random_epoch_between_oct2014_oct2017():
    return str(1412202241000 + random.randrange(1000, 94694400000))

def add_random_data_to_table(num_items, dynamo_table):
    """ Seeds DynamoDB table with random data """
    counter = 0
    while counter < num_items:
        company_and_id = random.choice(COMPANIES_AND_IDS)
        service = random.choice(['development', 'infrastructure-design', 'security-analysis', 'database-migration'])
        epoch = random_epoch_between_oct2014_oct2017()
        dynamo_table.put_item(
            Item={
                'clientId': company_and_id[1], # Company Id
                'timestamp': epoch,
                'clientName': company_and_id[0], # Company name
                'serviceType': service,
                'serviceId': service + '_' + company_and_id[1] + '_' + epoch,
                'cost': random.randrange(5000, 1000000, 500)
            }
        )
        time.sleep(0.1)
        counter += 1

def add_test_val_for_student_to_check_for()
    dynamo_table.put_item(
            Item={
                'clientId': 'protowtires',
                'timestamp': '1508961438000',
                'clientName': 'ProTowTires',
                'serviceType': 'development',
                'serviceId': 'development_protowtires_1508961438000',
                'cost': '5000'
            }
        )

def add_test_val_for_us_to_check_for()
    dynamo_table.put_item(
            Item={
                'clientId': 'toystoystoys',
                'timestamp': '1508961438000',
                'clientName': 'Toys Toys Toys',
                'serviceType': 'development',
                'serviceId': 'development_toystoystoys_1508961438000',
                'cost': '10000'
            }
        )


# Add some random data to the table 
def handler(event, context):
    print(event)
    print(context)
    
    # Handles the case when this is called during deletion
    if event['RequestType'] == 'Delete':
        cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})
        return 'SUCCESS'
    
    service_record_table = boto3.resource('dynamodb').Table('PrometheonServiceRecords')
    
    add_random_data_to_table(245, service_record_table)

    # Return resposne to CloudFormation saying this was successful
    cf_response.send(event, context, 'SUCCESS', {'Status': 'SUCCESS'})