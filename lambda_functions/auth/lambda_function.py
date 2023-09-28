import os
import jwt
import datetime
from http import HTTPStatus

SECRET_KEY = os.getenv('SECRET_KEY') # NOT GETTING THE KEY EXPORTED - WHY?


def lambda_handler(event, context):
    try:
        print(f"{os.environ=}")
        print(f"{SECRET_KEY=}")

        token = jwt.encode(
            {"exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return {
            "statusCode": HTTPStatus.OK,
            "body": {"token": token}
        }
    except Exception as e:
        return {"statusCode": HTTPStatus.INTERNAL_SERVER_ERROR, "body": str(e)}
