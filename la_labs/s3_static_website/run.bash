#!/bin/bash

aws cloudformation create-stack --stack-name sls2-s5-lab1-static-site --template-body file://mycf.json --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM