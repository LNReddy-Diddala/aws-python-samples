import boto3
from botocore.exceptions import ClientError


def main():

	REGION = 'us-east-2'
	# Create an S3 client
	s3 = boto3.client('s3')
	#list_s3_buckets(s3)
	create_s3_bucket(s3, 'test-bucket-msr560', REGION)
	#list_s3_buckets(s3)

# Get list of buckets
def list_s3_buckets(s3):
	
	# Call S3 list buckets
	response = s3.list_buckets()

	# Get a list of all bucket names from the response
	buckets = [bucket['Name'] for bucket in response['Buckets']]

	# Print out the buckets list
	print("Buckets list: {buckets_list}".format(buckets_list=buckets))

# Create new bucket, if bucket not existed.
def create_s3_bucket(s3, bucket_name, REGION):

	try:
		response = s3.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = {'LocationConstraint': REGION})
		if response['ResponseMetadata']['HTTPStatusCode'] == 200:
			print("{bucket} bucket is created successfully.".format(bucket = bucket_name))

	except ClientError as e:

		if e.response['Error']['Code'] == 'BucketAlreadyExists':
			print(e.response['Error']['Message'])
		elif e.response['Error']['Code'] == 'IllegalLocationConstraintException':
			print(e.response['Error']['Message'])
		else:
			print(e.response)

# Upload file to the bucket
def upload_file_to_bucket():
	pass

# Download file from bucket
def upload_file_to_bucket():
	pass

# Delete file from bucket
def delete_file_from_bucket():
	pass

# Delete bucket, if bucket exist
def delete_bucket():
	pass


if __name__ == '__main__':
	main()