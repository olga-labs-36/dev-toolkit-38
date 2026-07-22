import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_positive_integer(value):
    return isinstance(value, int) and value > 0


def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


def validate_user_data(data):
    if not is_valid_email(data.get('email', '')):
        return False, 'Invalid email address'
    if not is_positive_integer(data.get('age')):
        return False, 'Age must be a positive integer'
    if not is_non_empty_string(data.get('username')):
        return False, 'Username cannot be empty'
    return True, 'Validation successful'