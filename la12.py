import boto3

# connect to aws s3
client = boto3.client('s3')

# my first bucket
response = client.create_bucket(
   
    Bucket='raw-finance-data-20262000',
   
)
# my second bucket for processed data
response = client.create_bucket(
   
    Bucket='proceed-finance-data-20262000',
   
)
# my third bucket for final data
response = client.create_bucket(
   
    Bucket='final-finance-data-20262000',
   
)
# these are the list of my bucket
buckets = ['raw-finance-data-20262000', 'proceed-finance-data-20262000', 'final-finance-data-20262000']
# here we apply for loop to provide encryption to each bucket
for name in buckets:
    client.put_bucket_encryption(
        Bucket=name,
        ServerSideEncryptionConfiguration={
            'Rules': [{
                'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'aws:kms'},
                'BucketKeyEnabled': True
            }]
        }
    )
# here i am uploading file insid my raw data bucket

client.upload_file('la_ch_ma.pdf', 'raw-finance-data-20262000', 'hell.pdf')


