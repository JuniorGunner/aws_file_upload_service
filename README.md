# 📁 AWS File Upload Service
## 🚀 Overview

This is a robust and scalable File Upload Service built with ☁️ AWS Lambda and S3. It allows users to effortlessly upload, download, and delete files from the cloud storage - all with a secure and user-friendly interface.

## 🌟 Features
- 🔐 User registration and authentication
- 📤 File upload
- 📥 File download
- 🗑️ File deletion


## Tech Stack 🛠️
Our service leverages a variety of powerful technologies:

- 🐍 Python
- ☁️ AWS Lambda
- ☁️ AWS S3
- ⚙️ AWS SAM for local development and deployment
- ⚙️ Github Actions

## 🏗 Project Structure

```
/project_root
    /lambda_functions
        /auth
            lambda_function.py
        /upload
            lambda_function.py
        /download
            lambda_function.py
        /delete
            lambda_function.py
    /tests
        test_functions.py
    template.yaml
    requirements.txt
    .github/workflows/main.yml
```

## ⚙️ Installation and Setup

1. Clone the repository
```
git clone <repository-url>
```

2. Navigate to the project directory
```
cd <project-dir>
```

3. Install the Requirements
```
pip install -r requirements.txt
```

4. Install AWS SAM CLI
Follow the instructions here to install the AWS SAM CLI.

5. Install Docker
Follow the instructions here to install Docker as it is required to run AWS Lambda functions locally.

## Running Locally with SAM
After setting up, navigate to your project root directory in the terminal and use the SAM CLI to invoke the functions locally.

Start the API Gateway locally
```
sam local start-api
```

* After starting the local API Gateway, you can send HTTP requests to the locally running API, for example, using curl or Postman.

## 🧪 Running Tests
Navigate to your project root directory and run:
```
pytest tests/
```

## 🌐 Deploying

Deployment is handled via GitHub Actions which use AWS SAM to build, package, and deploy the application.

Make sure to setup GitHub Secrets in your repository to store AWS Access Key ID, AWS Secret Access Key, and any other sensitive information securely.

### Note:
Please store sensitive data like JWT Secret Keys in AWS Secrets Manager for production.
When testing locally with SAM and Docker, ensure Docker is running.
It is recommended to understand the AWS Free Tier limitations to avoid incurring additional costs.
