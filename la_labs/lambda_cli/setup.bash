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
aws s3 mv ./package.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/sls2_s3_lab2_lambda_cli_datalaoder.zip --acl public-read

echo "Packaging all the other Lambda functions to s3"
zip ./create.zip ./api_functions/create.js
zip ./get.zip ./api_functions/get.js
zip ./update.zip ./api_functions/update.js
zip ./delete.zip ./api_functions/delete.js
zip ./list.zip ./api_functions/list.js

aws s3 mv ./create.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/create.zip --acl public-read
aws s3 mv ./get.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/get.zip --acl public-read
aws s3 mv ./update.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/update.zip --acl public-read
aws s3 mv ./delete.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/delete.zip --acl public-read
aws s3 mv ./list.zip s3://cloudassessments-lab-files/aws/s3/lambda_cli_practical/list.zip --acl public-read

rm ./create.zip
rm ./get.zip
rm ./update.zip
rm ./delete.zip
rm ./list.zip