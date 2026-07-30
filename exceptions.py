import time
import functools

class NetworkError(Exception):
    pass

def retry(max_retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    if attempt < max_retries - 1:
                        time.sleep(delay)
                    else:
                        raise e
        return wrapper
    return decorator

@retry(max_retries=5, delay=1)
def fetch_data(url):
    # Simulate network operation
    if random.random() < 0.7:
        raise NetworkError('Failed to fetch data')
    return {'data': 'sample data'}
