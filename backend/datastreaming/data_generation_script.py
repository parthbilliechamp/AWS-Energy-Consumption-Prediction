import boto3
from datetime import datetime
import time
import calendar
import json
import os

AWS_ACCESS_KEY_ID = os.getenv('AWSACCESSKEYID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWSSECRETACCESSKEY')
AWS_SESSION_TOKEN = os.getenv('AWSSESSIONTOKEN')
AWS_REGION_NAME = os.getenv('AWSREGIONNAME')

def _get_kinesis_object():
    return boto3.client('firehose',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                aws_session_token=AWS_SESSION_TOKEN,
                region_name=AWS_REGION_NAME)

data = [{
            "DateAndTime": "2007-06-30 10:00:00",
            "sm1": "140.0",
            "sm2": "230.0",
            "sm3": "542.0"
        },
        {
            "DateAndTime": "2007-06-30 11:00:00",
            "sm1": "1034.0",
            "sm2": "434.0",
            "sm3": "45.0"
        },
        {
            "DateAndTime": "2007-06-30 12:00:00",
            "sm1": "123.0",
            "sm2": "443.0",
            "sm3": "34.0"
        },
        {
            "DateAndTime": "2007-06-30 13:00:00",
            "sm1": "34.0",
            "sm2": "55.0",
            "sm3": "54.0"
        },
        {
            "DateAndTime": "2007-06-30 14:00:00",
            "sm1": "324.0",
            "sm2": "54.0",
            "sm3": "112.0"
        },
        {
            "DateAndTime": "2007-06-30 15:00:00",
            "sm1": "455.0",
            "sm2": "54.0",
            "sm3": "55.0"
        },
        {
            "DateAndTime": "2007-06-30 16:00:00",
            "sm1": "778.0",
            "sm2": "80.0",
            "sm3": "147.0"
        },
        {
            "DateAndTime": "2007-06-30 17:00:00",
            "sm1": "530.0",
            "sm2": "55.0",
            "sm3": "1050.0"
        },
        {
            "DateAndTime": "2007-06-30 18:00:00",
            "sm1": "435.0",
            "sm2": "22.0",
            "sm3": "1064.0"
        },
        {
            "DateAndTime": "2007-06-30 19:00:00",	
            "sm1": "1216.0",
            "sm2": "10.0",
            "sm3": "1054.0"
        },
        {
            "DateAndTime": "2007-06-30 20:00:00",
            "sm1": "525.0",
            "sm2": "72.0",
            "sm3": "1052.0"
        },
        {
            "DateAndTime": "2007-06-30 21:00:00",
            "sm1": "112.0",
            "sm2": "47.0",
            "sm3": "1059.0"
        },
        {
            "DateAndTime": "2007-06-30 22:00:00",
            "sm1": "112.0",
            "sm2": "43.0",
            "sm3": "500.0"
        },
        {
            "DateAndTime": "2007-06-30 23:00:00",
            "sm1": "158.0",
            "sm2": "332.0",
            "sm3": "556.0"
        },
        ]

def start_data_generation(kinesis):
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())

    payload = {
        'timestamp': str(property_timestamp),
        'data': data
    }
    response = kinesis.put_record(DeliveryStreamName='energyconsumptionstream', Record={'Data': json.dumps(payload)})
    print(response)

def get_session():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION_NAME
    )
    return session

def main():
    kinesis = _get_kinesis_object()
    start_data_generation(kinesis)

if __name__ == "__main__":
    main()
