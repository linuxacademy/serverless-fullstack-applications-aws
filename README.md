This repo will host demo files for the Developing Fullstack Serverless Applications on AWS Quest for Cloud Assessments.

# Instructions for lab deployment

## TLDR

0. Make sure you have Python 3.6 installed locally
1. Create an AWS s3 bucket for the lambda function package (we've done this already at cloudassessments-lab-files/aws/s3/dynamodb_console_practical)
2. Run the setup.bash script to output to the bucket (this needs to happen once whenever the lambda function gets updated)
3. Make the lambda package files in the bucket publicly readable so each lab environment can grab them
4. Modify `mycf.json` to read from the bucket
5. Create the stack with `run.sh` or however else you'd like to create it.
6. Delete the stack however you'd like to delete it.