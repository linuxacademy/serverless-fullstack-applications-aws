#!/bin/bash

aws cloudformation create-stack --stack-name sls2_s2_lab2_dynamodb_node_sdk --template-body file://mycf.json --capabilities CAPABILITY_IAM