import boto3
from botocore.exceptions import ClientError


REGION = 'us-east-2'
BUCKET_NAME = 'test-bucket-msr560'
UPLOAD_FILE_PATH = '/home/msr/s3-python-test_latest.txt' #Place your file-pathe along with file-name
UPLAOD_FILE_NAME = 's3-python-test_latest.txt'
FILE_NAME_IN_S3 = 's3-python-test_latest.txt'
DOWNLOAD_FILE_NAME = 's3-python-test_latest.txt'
DELETE_FILE_NAME = 's3-python-test_latest.txt'
DELETE_BUCKET_NAME = 'test-bucket-msr560'

def main():

	# Create an S3 client
	s3 = boto3.client('s3')
	list_s3_buckets(s3)
	create_s3_bucket(s3, BUCKET_NAME, REGION)
	#upload_file_to_bucket(s3, UPLOAD_FILE_PATH, BUCKET_NAME, UPLAOD_FILE_NAME)
	#download_file_from_bucket(BUCKET_NAME, FILE_NAME_IN_S3, UPLAOD_FILE_NAME)
	#list_s3_buckets(s3)
	#delete_file_from_bucket(BUCKET_NAME, DELETE_FILE_NAME) # Still pending------>
	#delete_bucket(DELETE_BUCKET_NAME)
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
			print('"{bucket}" bucket has been created successfully.'.format(bucket = bucket_name))

	except ClientError as e:
			print(e.response['Error']['Message'])

# Upload file to the bucket
def upload_file_to_bucket(S3, file_path, bucket_name, file_name):

	S3.upload_file(file_path, bucket_name, file_name)
	print('"{file_name}" file has been uploaded to "{bucket}" bucket successfully'.format(file_name = file_name, bucket = bucket_name))
	

# Download file from bucket
def download_file_from_bucket(bucket_name, file_name_in_s3, file_name):

	s3 = boto3.resource('s3')

	try:
		s3.Bucket(bucket_name).download_file(file_name_in_s3, file_name)
		print('"{file_name}" file has been downloaded from "{bucket} successfully"'.format(file_name = file_name_in_s3, bucket = bucket_name))

	except ClientError as e:

	    if e.response['Error']['Code'] == "404":
	        print("The object does not exist.")
	    else:
	        raise


# Delete file from bucket
def delete_file_from_bucket(bucket_name, delete_file_name):
	s3 = boto3.resource('s3')

	try:
		s3.Bucket(bucket_name).delete_objects(delete_file_name)
		print('"{file_name}" file has been deleted from "{bucket} successfully"'.format(file_name = delete_file_name, bucket = bucket_name))

	except ClientError as e:

	    if e.response['Error']['Code'] == "404":
	        print("The object does not exist.")
	    else:
	        raise

# Delete bucket, if bucket exist
def delete_bucket(bucket_name):

	try:
		s3 = boto3.resource('s3')
		bucket = s3.Bucket(bucket_name)
		for key in bucket.objects.all():
			key.delete()

		response = bucket.delete()

		if response['ResponseMetadata']['HTTPStatusCode'] == 204:
			print('"{bucket}" bucket has been deleted successfully.'.format(bucket = bucket_name))

	except ClientError as e:
		print(e.response['Error']['Message'])



if __name__ == '__main__':
	main()