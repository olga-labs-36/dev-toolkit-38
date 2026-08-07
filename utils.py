import time
import requests

class RetryException(Exception):
    pass

def retry_request(func, retries=3, delay=1, *args, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except (requests.ConnectionError, requests.Timeout) as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise RetryException(f'Request failed after {retries} attempts') from e

# Example usage
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()