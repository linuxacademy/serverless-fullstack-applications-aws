#!/bin/bash

aws cloudformation create-stack --stack-name sls2-s3-lab1-lambda-console-practical --template-body file://mycf.json --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM