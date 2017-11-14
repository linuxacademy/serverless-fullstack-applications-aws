#!/bin/bash

aws cloudformation create-stack --stack-name sls2-s4-lab1-api-gateway --template-body file://mycf.json --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM