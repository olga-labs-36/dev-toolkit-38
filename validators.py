import re

class ValidationError(Exception):
    pass

def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string.')
    if not email:
        raise ValidationError('Email cannot be empty.')
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email):
        raise ValidationError('Invalid email format.')
    return True

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer.')
    if age < 0:
        raise ValidationError('Age cannot be negative.')
    return True

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string.')
    if not username:
        raise ValidationError('Username cannot be empty.')
    if len(username) < 3:
        raise ValidationError('Username must be at least 3 characters long.')
    return True