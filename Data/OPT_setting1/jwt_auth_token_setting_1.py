import jwt
import datetime

secret_key = "your-256-bit-secret"
user_id = "123456"

payload = {
    "user_id": user_id,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)

