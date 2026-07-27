import time
import requests


def retry_request(url, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            attempt += 1
            time.sleep(delay)
    return None


if __name__ == '__main__':
    url = 'https://api.example.com/data'
    result = retry_request(url)
    if result:
        print('Success:', result.json())
    else:
        print('Failed to fetch data after retries.')