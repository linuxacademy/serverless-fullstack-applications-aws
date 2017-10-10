#!/bin/bash

aws cloudformation create-stack --stack-name sls1-s2-lab4-dynmodb-aws-sdk --template-body file://mycf.json --capabilities CAPABILITY_IAM