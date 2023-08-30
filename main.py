import os

# library to read passwords
from dotenv import load_dotenv
load_dotenv()

# import etl functions
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_data_to_s3 import df_to_s3

# load passwords from .env file
dbname = os.getenv('dbname')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key_id = os.getenv('aws_secret_access_key_id')

# run function to extract and clean online transactions data as per request
transactional_data = extract_transactional_data(dbname, host, port, user, password)
print('The shape of the extracted and cleaned data is: ',transactional_data.shape)

# run function to find and remove duplicates
duplicates = identify_and_remove_duplicates(transactional_data)
print('The shape of the data after removing duplicates is: ',duplicates.shape)

# run function to connect and load data to s3 with provided credentials

s3_bucket = 'july-bootcamp'
key = 'etl_pipeline/iz_online_transaction_v2.pkl'
df = transactional_data

df_to_s3(df, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)