import boto3
import pandas as pa

client = boto3.client('s3')

client.download_file('raw-finance-data-20262000', 'hell.csv', 'data.csv')
df = pa.read_csv('data.csv', encoding='latin1', sep=None, engine='python', on_bad_lines='skip')

#now you have to cleaned the csv
df.dropna(inplace = True)

df.to_csv('cleaned_data.csv', index = False)

client.upload_file('cleaned_data.csv', 'proceed-finance-data-20262000', 'hello.pdf')


