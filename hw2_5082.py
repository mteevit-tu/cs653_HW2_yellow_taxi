# -*- coding: utf-8 -*-
"""hw2_5082.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_YpocqVoeUNneYbbnZrKECF-2jF-Zi3R
"""

import boto3
import botocore
import pandas as pd
from IPython.display import display, Markdown

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

# define function for bucket creating
def create_bucket(bucket):
    import logging

    try:
        s3.create_bucket(Bucket = bucket)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return 'Bucket ' + bucket + ' could not be created.'
    return 'Created or already exists ' + bucket + ' bucket.'
# create bucket named 'nyctlc-cs653-5082'
create_bucket('nyctlc-cs653-5082')

# define function for key checking
def key_exists(bucket, key):
    try:
        s3_resource.Object(bucket, key).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # The key does not exist.
            return(False)
        else:
            # Something else has gone wrong.
            raise
    else:
        # The key does exist.
        return(True)

# define function for duplicating data from existing bucket to personal bucket 
def copy_among_buckets(from_bucket, from_key, to_bucket, to_key):
    if not key_exists(to_bucket, to_key):
        s3_resource.meta.client.copy({'Bucket': from_bucket, 'Key': from_key}, 
                                        to_bucket, to_key)        
        print('File {} saved to S3 bucket {}'.format(to_key, to_bucket))
    else:
	print('File {} already exists in S3 bucket {}'.format(to_key, to_bucket)) 

# bucket duplicating -> Jan 2017 to Mar 2017
copy_among_buckets(from_bucket='nyc-tlc', from_key = 'trip data/yellow_tripdata_2017-01.parquet',
                      to_bucket='nyctlc-cs653-5082', to_key='trip-data/yellow_2017-01.parquet')
copy_among_buckets(from_bucket='nyc-tlc', from_key = 'trip data/yellow_tripdata_2017-02.parquet',
                      to_bucket='nyctlc-cs653-5082', to_key='trip-data/yellow_2017-02.parquet')
copy_among_buckets(from_bucket='nyc-tlc', from_key = 'trip data/yellow_tripdata_2017-03.parquet',
                      to_bucket='nyctlc-cs653-5082', to_key='trip-data/yellow_2017-03.parquet')

# define a variable bucket to my bucket tag
bucket = 'nyctlc-cs653-5082'

# Question 1
print('----------------------------')
print('An Answer for Question 1')
print('----------------------------')
for i in range(1,6):
    s3_select_results = s3.select_object_content(
        Bucket=bucket,
        Key='trip-data/yellow_2017-01.parquet',
        Expression="SELECT count(payment_type) FROM s3object s WHERE payment_type = {}".format(i),
        ExpressionType='SQL',
        InputSerialization={'Parquet': {}},
        OutputSerialization={'CSV': {}},
    )

    for event in s3_select_results['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
    print("No. of payment_type {} = {}".format(i, records))

print('----------------------------')
print('')

# Question 2
print('----------------------------')
print('An Answer for Question 2')
print('----------------------------')
for i in range(1,266):
    s3_select_results_countloc = s3.select_object_content(
        Bucket=bucket,
        Key='trip-data/yellow_2017-01.parquet',
        Expression="SELECT count(PULocationID) FROM s3object s WHERE PULocationID = {}".format(i),
        ExpressionType='SQL',
        InputSerialization={'Parquet': {}},
        OutputSerialization={'CSV': {}},
    )
    s3_select_results_sumfare = s3.select_object_content(
        Bucket=bucket,
        Key='trip-data/yellow_2017-01.parquet',
        Expression="SELECT sum(fare_amount) FROM s3object s WHERE PULocationID = {}".format(i),
        ExpressionType='SQL',
        InputSerialization={'Parquet': {}},
        OutputSerialization={'CSV': {}},
    )
    s3_select_results_avgpass = s3.select_object_content(
        Bucket=bucket,
        Key='trip-data/yellow_2017-01.parquet',
        Expression="SELECT avg(passenger_count) FROM s3object s WHERE PULocationID = {}".format(i),
        ExpressionType='SQL',
        InputSerialization={'Parquet': {}},
        OutputSerialization={'CSV': {}},
    )
    for event in s3_select_results_countloc['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            records = int(records)
    print("No. of rides in Location {} = {}".format(i, records))
    for event in s3_select_results_sumfare['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            records = float(records)
    print("Sum fare amount in Location {} = {:.2f}".format(i, records))
    for event in s3_select_results_avgpass['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8') 
            records = float(records)
    print("Average no. of passenger in Location {} = {:.2f}".format(i, records))
    print("---")

# Question 3
print('----------------------------')
print('An Answer for Question 3')
print('----------------------------')
for month in range(1,4):
    print("2017, Month: {}".format(month))
    for type in range(1,6):
        s3_select_results_3m = s3.select_object_content(
            Bucket=bucket,
            Key="trip-data/yellow_2017-0{}.parquet".format(month),
            Expression="SELECT count(payment_type) FROM s3object s WHERE payment_type = {}".format(type),
            ExpressionType='SQL',
            InputSerialization={'Parquet': {}},
            OutputSerialization={'CSV': {}},
        )
	for event in s3_select_results_3m['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                records = float(records)
        print("No. of payment_type {} = {}".format(type, records))
    print("---")