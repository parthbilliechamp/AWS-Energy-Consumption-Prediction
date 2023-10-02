
# Household Energy Consumption System

## AWS Cloud-based web application that predicts household energy consumption based on a Machine Learning model.

<p align="center">
<img width="640px"  src="https://parthchampaneria-portfolio.s3.amazonaws.com/triviahomepage.png" alt="">
<p>

- [Introduction & Goals](#introduction--goals)
- [Project Architecture](#project-architecture)
- [Tools and Technologies used](#tools)
- [Services used](#services-used)
  - [User Authentication and Authorization](#User-Authentication-and-Authorization)
  - [User Profile Management](#User-Profile-Management)
  - [Game LeaderBoard](#Game-LeaderBoard)
  - [Team Management](#Team-Management)
  - [Chat Bot for Virtual assistance](#Chat-Bot-for-Virtual-assistance)
  - [Admin Dashboard](#Admin-Dashboard)
  - [Game Module](#Game-Module)
  - [Notifications and Alerts](#Notifications-and-Alerts)
- [Deployment Pipeline](#deployment-pipeline)
- [Project Demo](#project-demo)
- [Author: 👤 **Parth Champaneria**](#author--parth-champaneria)
- [Show your support](#show-your-support)


# Introduction & Goals


**Main goals:**
The main goal of this project is to provide users with accurate predictions of household energy consumption and empower them to make informed decisions about their energy usage.

# Project architecture

<p align="center">
<img width="720px"  src="https://projects-mediahouse.s3.amazonaws.com/trivia-serverless/architecture.png" alt="">
<p>


# Tools

  - Python and its libraries - Pandas, Requests, boto3, NumPy, Scikit
    - For implementing the backend services and creating ML models
  
  - [Docker](https://www.docker.com/) 
    - For deployment of the application
   
  - [React JS](https://react.dev/)
    - For developing the front end of the application
      
  - [Visual Studio Code](https://code.visualstudio.com/)
    - IDE for development


# Services used


## Compute Services used:

- Docker and AWS Elastic Beanstalk – Run a web app with the Docker platform in a container.
- AWS Lambda - Functions that run without the server.

## Storage Services used:

- AWS S3 – Simple file storage.
- AWS DynamoDB – NoSQL database.

## Network Services used:

- AWS API Gateway – Secure and route API requests to lambdas or container APIs.

## General Services used:

- AWS Kinesis – Capture data streams.
- AWS Cognito - Managing application users.


# Deployment Pipeline

A CI/CD pipeline has been configured for deploying the React-based frontend application, containerized with Docker and hosted on Google Cloud Platform's Cloud Run, as depicted in the figure below

<p align="center">
<img width="640px"  src="https://projects-mediahouse.s3.amazonaws.com/trivia-serverless/deployment-pipeline.png" alt="">
<p>

# Project Demo

- The project demo can be viewed [here](https://projects-mediahouse.s3.amazonaws.com/trivia-serverless/demo.mp4)


# Author: 👤 **Parth Champaneria**

# Show your support

Give a ⭐️ if this project helped you!
