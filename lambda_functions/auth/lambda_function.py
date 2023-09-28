import jwt
import datetime
import http

SECRET_KEY = "YOUR_SECRET_KEY"  # Store in AWS Secrets Manager in production

def lambda_handler(event, context):
    try:
        token = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)}, SECRET_KEY, algorithm="HS256")
        return {
            "statusCode": http.HTTPStatus.OK,
            "body": {"token": token}
        }
    except Exception as e:
        return {"statusCode": http.HTTPStatus.INTERNAL_SERVER_ERROR, "body": str(e)}
