import re

def validate_email(email):
    regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(regex, email) is not None


def validate_phone(phone):
    regex = r'^\+?1?\d{9,15}$'
    return re.match(regex, phone) is not None


def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_url(url):
    regex = r'^(https?://)?(www\.)?([a-z0-9-]+\.[a-z]{2,})(/[\w-./?%&=]*)?$'
    return re.match(regex, url) is not None


def validate_username(username):
    return 3 <= len(username) <= 30 and username.isalnum()