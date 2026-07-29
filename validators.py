import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def is_valid_age(age):
    return isinstance(age, int) and 0 <= age <= 120


def validate_user_input(email, age):
    if not is_valid_email(email):
        raise ValueError('Invalid email format')
    if not is_valid_age(age):
        raise ValueError('Age must be an integer between 0 and 120')
    return True