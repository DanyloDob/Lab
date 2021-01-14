from contextlib import contextmanager
from functools import wraps

from flask import jsonify
#from flask_jwt import current_identity


from schemas import StatusResponse


def only_admin_access(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not current_identity.is_admin:
            return jsonify(StatusResponse().dump({
                "code": 401,
                "type": "NOT_AUTHORIZED",
                "message": "Only Admin is allowed to access",
            })), 401
        return func(*args, **kwargs)
    return inner


def only_target_user_access_or_admin(func):
    @wraps(func)
    def inner(user_id, *args, **kwargs):
        if current_identity.id != user_id and not current_identity.is_admin:
            return jsonify(StatusResponse().dump({
                "code": 401,
                "type": "NOT_AUTHORIZED",
                "message": f"Authorize and come!",
            })), 401
        return func(user_id, *args, **kwargs)
    return inner