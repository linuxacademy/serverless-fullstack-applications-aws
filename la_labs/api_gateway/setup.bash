#!/bin/bash

# Assumes python v3.6
# Create and initialize a Python Virtual Environment
echo "Creating a virtual environment called .env and starting it."
python3.6 -m venv .env && source .env/bin/activate

echo "Creating 'setup' directory and moving relevant files in there"
mkdir setup
cp dynamo_autofill.py setup/
cp cf_response.py setup/
cp musicData.json setup/

echo "pip installing requirements from requirements file in target directory"
cd ./setup
pip3 install -r ../requirements.txt -t .

echo "Zipping package for deployment"
zip -r ../package.zip ./* 

echo "Removing setup directory and virtual environment"
cd ..
rm -r ./setup
deactivate
rm -r ./.env

echo "Deploying 'package.zip' to AWS"
aws s3 mv ./package.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/sls2_s4_lab1_api_gateway_datalaoder.zip --acl public-read

echo "Packaging all the other Lambda functions to s3"
zip -j ./create.zip ./api_functions/create.js
zip -j ./get.zip ./api_functions/get.js
zip -j ./update.zip ./api_functions/update.js
zip -j ./delete.zip ./api_functions/delete.js
zip -j ./list.zip ./api_functions/list.js

aws s3 mv ./create.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/create.zip --acl public-read
aws s3 mv ./get.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/get.zip --acl public-read
aws s3 mv ./update.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/update.zip --acl public-read
aws s3 mv ./delete.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/delete.zip --acl public-read
aws s3 mv ./list.zip s3://cloudassessments-lab-files/aws/s3/api_gateway/list.zip --acl public-read