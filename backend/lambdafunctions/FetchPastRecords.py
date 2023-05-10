import json
from datetime import datetime
import pandas as pd
import boto3
from boto3.dynamodb.conditions import Attr
import os

AWS_ACCESS_KEY_ID = os.getenv('AWSACCESSKEYID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWSSECRETACCESSKEY')
AWS_SESSION_TOKEN = os.getenv('AWSSESSIONTOKEN')
AWS_REGION_NAME = os.getenv('AWSREGIONNAME')


def lambda_handler(event, context):
    start_date = event["queryStringParameters"]["startDate"]
    end_date = event["queryStringParameters"]["endDate"]
    start_date = datetime.fromisoformat(start_date.replace(
        "Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")
    end_date = datetime.fromisoformat(end_date.replace(
        "Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")
    print(start_date)
    print(end_date)
    dynamodb = _get_dynamo_db_object()

    table = dynamodb.Table('energyconsumptionhistorytable')
    response = table.scan(
        FilterExpression=Attr('DateAndTime').between(start_date, end_date)
    )
    items = response.get('Items', [])
    df = pd.DataFrame(items)

    if df.empty:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            'body': json.dumps(
                {"message": "No data"}
            ),
            "isBase64Encoded": False
        }

    df['DateAndTime'] = pd.to_datetime(df['DateAndTime'])
    df['Sub_metering_1'] = pd.to_numeric(df['Sub_metering_1'])
    df['Sub_metering_2'] = pd.to_numeric(df['Sub_metering_2'])
    df['Sub_metering_3'] = pd.to_numeric(df['Sub_metering_3'])

    result_bar_graph = _get_result_for_bar_graph(df)
    result_pie_chart = _get_result_for_pie_chart(df)
    result_line_graph = _get_result_for_line_graph(df)

    response = {'bar_graph_data': result_bar_graph,
                'pie_chart_data': result_pie_chart,
                'line_graph_data': result_line_graph}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        'body': json.dumps(
            response
        ),
        "isBase64Encoded": False
    }


def get_session():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION_NAME
    )
    return session


def _get_dynamo_db_object():
    print(get_session())
    return get_session().resource('dynamodb')


def _get_result_for_bar_graph(df):
    df_monthly = df.groupby(pd.Grouper(key='DateAndTime', freq='M')).sum()
    df_monthly.index = df_monthly.index.strftime('%B')
    df_new = df_monthly.reset_index()
    list = []
    for _, row in df_new.iterrows():
        json_dict = row.to_dict()
        list.append(json_dict)
    return list


def _get_result_for_pie_chart(df):
    sum_sub_metering_1 = df['Sub_metering_1'].sum()
    sum_sub_metering_2 = df['Sub_metering_2'].sum()
    sum_sub_metering_3 = df['Sub_metering_3'].sum()
    return {'Sub_metering_1': sum_sub_metering_1,
            'Sub_metering_2': sum_sub_metering_2,
            'Sub_metering_3': sum_sub_metering_3
            }


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
