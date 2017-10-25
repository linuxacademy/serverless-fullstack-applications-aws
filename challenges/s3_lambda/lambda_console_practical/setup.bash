#!/bin/bash

# Assumes python v3.6
# Create and initialize a Python Virtual Environment
echo "Creating a virtual environment called .env and starting it."
python3.6 -m venv .env && source .env/bin/activate

echo "Creating 'setup' directory and moving relevant files in there"
mkdir setup
cp dynamo_autofill.py setup/
cp cf_response.py setup/

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
aws s3 mv ./package.zip s3://cloudassessments-lab-files/aws/s3/lambda_console_practical/sls1_s3_lab1_lambda_console_practical_datalaoder.zip --acl public-read