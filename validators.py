def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError('Missing or invalid name')
    if 'age' not in data or not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError('Missing or invalid age')
    return True

def main_loop(inputs):
    for data in inputs:
        try:
            validate_input(data)
            process_data(data)
        except ValueError as ve:
            print(f'Input error: {ve}')
        except Exception as e:
            print(f'Unexpected error: {e}')

def process_data(data):
    print(f'Processing {data['name']} who is {data['age']} years old')

inputs = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': -5},
    {'name': 'Charlie'},
    'Invalid Data',
]
main_loop(inputs)