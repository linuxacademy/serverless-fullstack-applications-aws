#!/bin/bash

aws cloudformation create-stack --stack-name sls1-dynamodb-console --template-body file://mycf.json --capabilities CAPABILITY_IAM