import pandas as pd
import lightgbm as lgb
import pickle
from flask import Flask, request, jsonify
import boto3
import os
from dotenv import load_dotenv
import boto3
import numpy as np
from io import StringIO
import json
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

AWS_ACCESS_KEY_ID = os.getenv('AWSACCESSKEYID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWSSECRETACCESSKEY')
AWS_SESSION_TOKEN = os.getenv('AWSSESSIONTOKEN')
AWS_REGION_NAME = os.getenv('AWSREGIONNAME')

# S3 details
bucket_name = "energyconsumptionhistory"
sm1_file_name = "model_sm1.pkl"
sm2_file_name = "model_sm2.pkl"
sm3_file_name = "model_sm3.pkl"


def get_s3_object():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION_NAME
    )
    return s3


@application.route('/test')
def test():
    response = {'message': 'Hello, World!'}
    return jsonify(response)


@application.route('/trainmodel')
def train_model():
    print("env variables")
    print(os.getenv("AWSACCESSKEYID"))
    energy_consumption_df = data_import()
    energy_consumption_df_cleaned = clean_data(energy_consumption_df)
    energy_consumption_df_processed = process_data(
        energy_consumption_df_cleaned)

    # training model for Sub_metering_1
    X_train, y_train = perform_feature_engineering_sm1(
        energy_consumption_df_processed)
    machine_learning_model = train(X_train, y_train)
    save_model(machine_learning_model, sm1_file_name)

    # training model for Sub_metering_2
    X_train, y_train = perform_feature_engineering_sm2(
        energy_consumption_df_processed)
    machine_learning_model = train(X_train, y_train)
    save_model(machine_learning_model, sm2_file_name)

    # training model for Sub_metering_3
    X_train, y_train = perform_feature_engineering_sm3(
        energy_consumption_df_processed)
    machine_learning_model = train(X_train, y_train)
    save_model(machine_learning_model, sm3_file_name)

    response = {'message': 'Model training completed successfully'}

    return jsonify(response)


@application.route('/performprediction', methods=['POST'])
def predict():
    data = request.get_json()

    sm1_model = load_model(sm1_file_name)
    sm2_model = load_model(sm2_file_name)
    sm3_model = load_model(sm3_file_name)

    sm1_feature_columns = create_feature_columns_sm1(data)
    sm2_feature_columns = create_feature_columns_sm2(data)
    sm3_feature_columns = create_feature_columns_sm3(data)

    print("feature columns : ")
    print(sm1_feature_columns)

    # start prediction
    yhat_sm1 = sm1_model.predict(sm1_feature_columns)
    yhat_sm2 = sm2_model.predict(sm2_feature_columns)
    yhat_sm3 = sm3_model.predict(sm3_feature_columns)

    print(yhat_sm1)
    print(yhat_sm2)
    print(yhat_sm3)

    arr = np.concatenate([yhat_sm1, yhat_sm2, yhat_sm3]).reshape(-1, 3)
    df = pd.DataFrame(
        arr, columns=['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])
    temp_df = pd.DataFrame(data).iloc[6:, :].reset_index()
    print(temp_df)
    print("*******")
    print(df)

    df['DateAndTime'] = temp_df['DateAndTime']
    save_prediction(df)

    response =  {"message": "Data successfully added to prediction sink!"}

    return jsonify(response)


def load_model(file_name):
    s3 = get_s3_object()
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    serialized_model = response['Body'].read()
    model = pickle.loads(serialized_model)
    return model


def create_feature_columns_sm1(data):
    df = pd.DataFrame(data)
    result_df, y = perform_feature_engineering_sm1(df)
    result_df['lag_Sub_metering_1_6'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_6'])
    result_df['lag_Sub_metering_1_5'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_5'])
    result_df['lag_Sub_metering_1_4'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_4'])
    result_df['lag_Sub_metering_1_3'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_3'])
    result_df['lag_Sub_metering_1_2'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_2'])
    result_df['lag_Sub_metering_1_1'] = pd.to_numeric(
        result_df['lag_Sub_metering_1_1'])
    return result_df


def create_feature_columns_sm2(data):
    df = pd.DataFrame(data)
    result_df, y = perform_feature_engineering_sm2(df)
    result_df['lag_Sub_metering_2_6'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_6'])
    result_df['lag_Sub_metering_2_5'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_5'])
    result_df['lag_Sub_metering_2_4'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_4'])
    result_df['lag_Sub_metering_2_3'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_3'])
    result_df['lag_Sub_metering_2_2'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_2'])
    result_df['lag_Sub_metering_2_1'] = pd.to_numeric(
        result_df['lag_Sub_metering_2_1'])
    return result_df


def create_feature_columns_sm3(data):
    df = pd.DataFrame(data)
    result_df, y = perform_feature_engineering_sm3(df)
    result_df['lag_Sub_metering_3_6'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_6'])
    result_df['lag_Sub_metering_3_5'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_5'])
    result_df['lag_Sub_metering_3_4'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_4'])
    result_df['lag_Sub_metering_3_3'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_3'])
    result_df['lag_Sub_metering_3_2'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_2'])
    result_df['lag_Sub_metering_3_1'] = pd.to_numeric(
        result_df['lag_Sub_metering_3_1'])
    return result_df


def get_session():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION_NAME
    )
    return session


def _get_dynamo_db_object():
    return get_session().resource('dynamodb')


def save_prediction(df):
    dynamodb = _get_dynamo_db_object()
    table = dynamodb.Table('prediction')

    for index, row in df.iterrows():
        response = table.put_item(
            Item={
                # Unique identifier for the item
                "KeyIndex": "predictions-" + str(row['DateAndTime']),
                "Sub_metering_1": abs(int(row['Sub_metering_1'])),
                "Sub_metering_2": abs(int(row['Sub_metering_2'])),
                "Sub_metering_3": abs(int(row['Sub_metering_3'])),
                "DateAndTime": row['DateAndTime']
            }
        )


def data_import():
    s3 = get_s3_object()
    s3_object = s3.get_object(
        Bucket=bucket_name, Key='household_power_consumption.csv')
    body = s3_object['Body']
    csv_string = body.read().decode('utf-8')
    return pd.read_csv(StringIO(csv_string))


def clean_data(energy_consumption_df):
    df_filtered = energy_consumption_df[energy_consumption_df['Global_active_power'] != '?']
    df_filtered['Global_active_power'] = df_filtered['Global_active_power'].astype(
        float)
    df_filtered['Global_reactive_power'] = df_filtered['Global_active_power'].astype(
        float)
    df_filtered['Voltage'] = df_filtered['Voltage'].astype(float)
    df_filtered['Global_intensity'] = df_filtered['Global_intensity'].astype(
        float)
    df_filtered['Sub_metering_1'] = df_filtered['Sub_metering_1'].astype(float)
    df_filtered['Sub_metering_2'] = df_filtered['Sub_metering_2'].astype(float)
    df_filtered['Sub_metering_3'] = df_filtered['Sub_metering_3'].astype(float)
    df_filtered['DateTime'] = pd.to_datetime(
        df_filtered['Date']) + pd.to_timedelta(df_filtered['Time'])
    df_filtered.drop(['index', 'Date', 'Time'], axis=1, inplace=True)
    return df_filtered


def process_data(energy_consumption_df):
    return energy_consumption_df.groupby(pd.Grouper(key='DateTime', freq='H')).sum()


def perform_feature_engineering_sm1(df):
    print(df)
    result_df = create_feature_lags(df['Sub_metering_1'], 'Sub_metering_1')
    feature_columns = ['lag_Sub_metering_1_6', 'lag_Sub_metering_1_5', 'lag_Sub_metering_1_4',
                       'lag_Sub_metering_1_3', 'lag_Sub_metering_1_2', 'lag_Sub_metering_1_1']
    target_column = ['lag_Sub_metering_1_0']

    X_train, y_train = result_df[feature_columns], result_df[target_column]
    return X_train, y_train


def perform_feature_engineering_sm2(df):
    print(df)
    result_df = create_feature_lags(df['Sub_metering_2'], 'Sub_metering_2')
    feature_columns = ['lag_Sub_metering_2_6', 'lag_Sub_metering_2_5', 'lag_Sub_metering_2_4',
                       'lag_Sub_metering_2_3', 'lag_Sub_metering_2_2', 'lag_Sub_metering_2_1']
    target_column = ['lag_Sub_metering_2_0']

    X_train, y_train = result_df[feature_columns], result_df[target_column]
    return X_train, y_train


def perform_feature_engineering_sm3(df):
    print(df)
    result_df = create_feature_lags(df['Sub_metering_3'], 'Sub_metering_3')
    feature_columns = ['lag_Sub_metering_3_6', 'lag_Sub_metering_3_5', 'lag_Sub_metering_3_4',
                       'lag_Sub_metering_3_3', 'lag_Sub_metering_3_2', 'lag_Sub_metering_3_1']
    target_column = ['lag_Sub_metering_3_0']

    X_train, y_train = result_df[feature_columns], result_df[target_column]
    return X_train, y_train


def create_feature_lags(df, col):
    lag_range = 7
    my_list = []
    for index in range(0, lag_range):
        my_list.append(df.shift(-index))

    agg = pd.concat(my_list, axis=1)
    agg.dropna(inplace=True)
    lag_columns = ["lag_" + col + "_" + str(i) for i in range(6, -1, -1)]
    lags_df = pd.DataFrame(agg.values, columns=lag_columns)
    return lags_df


def train(X_train, y_train):
    # Define the parameters for the LightGBM model
    params = {
        'boosting': 'gbdt',
        'objective': 'regression',
        'num_leaves': 31,
        'min_child_samples': 20,
        'max_depth': -1,
        'learning_rate': 0.05,
        'metric': 'rmse',
        'verbose': -1,
        'linear_tree': True,
        'num_iterations': 200
    }

    # Create the LightGBM dataset from the training data
    lgb_train = lgb.Dataset(X_train, y_train)

    # Use the same dataset for evaluation as well
    lgb_eval = lgb.Dataset(X_train, y_train, reference=lgb_train)

    # Train the model and use early stopping based on the validation set
    model = lgb.train(params, train_set=lgb_train, valid_sets=[
                      lgb_eval], early_stopping_rounds=50)

    return model


def save_model(model, file_name):
    s3 = get_s3_object()
    serialized_model = pickle.dumps(model)
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=serialized_model)
