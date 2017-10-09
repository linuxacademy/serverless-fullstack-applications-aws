# Instructions for Lab deployment

## TLDR

0. Make sure you have Python 3.6 installed locally
1. Create an AWS s3 bucket for the lambda function package
2. Modify the setup.sh file to output to the bucket
3. Modify `mycf.json` to read from the bucket
4. Create the stack with `run.sh` or however else you'd like to create it.
5. Delete the stack however you'd like to delete it.