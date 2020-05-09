# Standard library
from typing import List, Tuple
from datetime import datetime, timedelta
from functools import wraps

# 3rd party modules
import jwt
from werkzeug.exceptions import Unauthorized
from flask import request


MY_AWESOME_SECRET = "ABC123"


def create_jwt_token(user_id: int, username: str, roles: List = None) -> bytes:
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=3),
            'iat': datetime.utcnow(),
            'sub': dict(user_id=user_id, username=username),
            'roles': roles
        }
        return jwt.encode(
            payload,
            MY_AWESOME_SECRET,
            algorithm='HS256'
        )
    except Exception as e:
        print(e)


def decode_jwt_token(jwt_token: bytes) -> Tuple[str, str, str]:
    try:
        payload = jwt.decode(jwt_token, MY_AWESOME_SECRET, algorithms='HS256')
        return (payload['sub']['user_id'], payload['sub']['username'], payload['roles'])
    except jwt.ExpiredSignatureError:
        raise Unauthorized("Token has expired, please sign in again")
    except jwt.InvalidTokenError:
        raise Unauthorized("Token is invalid, please sign in again")


def authorized(roles: List = []):
    def assert_authorized(f):
        def wrapper(*args, **kwargs):
            _has_authorized_role(roles)
            return f(*args, **kwargs)
        return wrapper
    return assert_authorized


def _has_authorized_role(roles: List[str]) -> None:
    token: bytes = request.headers.get('Authorization')
    payload: Tuple = decode_jwt_token(token)
    for role in payload[2]:
        if role in roles:
            return
    raise Unauthorized("You don't have permission")
