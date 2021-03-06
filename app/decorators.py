from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import Role


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(403)
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def role_required(role_name):
    def decorator(f):
        @wraps(f)
        
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(403)
            _role = Role.query.filter_by(id=current_user.role_id).first()
            if _role.name != role_name:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator