#!/bin/bash

username="parthchamp169@gmail.com"
password="Parth@123"
email="parthchamp169@gmail.com"
user_pool_id="us-east-1_NuT28OWF5"

aws cognito-idp admin-set-user-password --user-pool-id $user_pool_id --username $username --password $password --permanent