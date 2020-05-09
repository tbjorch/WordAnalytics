# Standard library
from typing import List, Tuple

# Internal modules
from user_service.utils.auth import decode_jwt_token
from user_service.utils import make_json_response


def authorize(roles: List, token: bytes) -> None:
    decoded_token: Tuple[str, str, str] = decode_jwt_token(token)
    for role in roles:
        if role in decoded_token[2]:
            return make_json_response(
                dict(
                    status_code=200,
                    message="User is authorized"
                    )
                )
    return make_json_response(
        dict(
            status_code=401,
            message="User is unauthorized"
            )
        )
