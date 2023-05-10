import json
import pandas as pd
import boto3
from boto3.dynamodb.conditions import Attr
import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')


def lambda_handler(event, context):
    dynamodb = _get_dynamo_db_object()

    table = dynamodb.Table('predictiontable')
    response = table.scan(
        Limit=7
    )
    items = response.get('Items', [])
    df = pd.DataFrame(items)

    df['DateAndTime'] = pd.to_datetime(df['DateAndTime'])
    df['Sub_metering_1'] = pd.to_numeric(df['Sub_metering_1'])
    df['Sub_metering_2'] = pd.to_numeric(df['Sub_metering_2'])
    df['Sub_metering_3'] = pd.to_numeric(df['Sub_metering_3'])

    result = _get_result_for_line_graph(df)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            "Access-Control-Allow-Headers" : "Content-Type"
        },
        'body': json.dumps(
            result
        ),
        "isBase64Encoded": False
    }


def get_session():
    return boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION_NAME
    )


def _get_dynamo_db_object():
    return get_session().resource('dynamodb')


def _get_result_for_line_graph(df):
    df['DateAndTime'] = df['DateAndTime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df = df[['DateAndTime', 'Sub_metering_1',
             'Sub_metering_2', 'Sub_metering_3']]
    df_sorted = df.sort_values(by='DateAndTime', ascending=True)
    list = []
    for _, row in df_sorted.iterrows():
        json_dict = row.to_dict()
        list.append(json_dict)
    return list
