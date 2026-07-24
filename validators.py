import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    pattern = r'^[+]?[0-9]{1,4}?[-.\s]?\(?(\d{1,3})?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    return re.match(pattern, phone) is not None


def validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def validate_input(data):
    if not validate_email(data.get('email', '')):
        return False, 'Invalid email address'
    if not validate_phone(data.get('phone', '')):
        return False, 'Invalid phone number'
    if not validate_integer(data.get('age', '')):
        return False, 'Age must be an integer'
    return True, 'Input is valid'