This repo will host demo files for the Developing Fullstack Serverless Applications on AWS Quest for Cloud Assessments.

# Instructions for lab deployment

Some of the Challenge and Learning Activity labs have a specific setup that needs to happen before we can create the environment successfully. Usually this comes in the form of a Lambda function that runs during the CloudFormation step as a Custom::Resource. 

In order to support that you'll need to run the `setup.bash` script once for each function before it can be used. The script builds the Lambda function package and uploads it to S3. You will need python3.6 installed for this but otherwise shouldn't require anything else.

After you run `setup.bash` you will need to make the function package public so that any AWS accounts can reference it. Someone with access to the production account can also add this to the `setup.bash` script to save time later.

After these steps are done you should be able to use the cloudformation in `mycf.json` to create the environment (minus the user account).

## TLDR

0. Make sure you have Python 3.6 installed locally
1. Create an AWS s3 bucket for the lambda function package (we've done this already at cloudassessments-lab-files/aws/s3/dynamodb_console_practical)
2. Run the setup.bash script to output to the bucket (this needs to happen once whenever the lambda function gets updated)
3. Make the lambda package files in the bucket publicly readable so each lab environment can grab them
4. Modify `mycf.json` to read from the bucket
5. Create the stack with `run.sh` or however else you'd like to create it.
6. Delete the stack however you'd like to delete it.