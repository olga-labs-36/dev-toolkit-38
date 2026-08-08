def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    required_keys = ['name', 'age']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required key: {key}')
    if not isinstance(data['name'], str) or not data['name']:
        raise ValueError('Name must be a non-empty string')
    if not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError('Age must be a non-negative integer')
    return True

def main_process_loop(data_list):
    results = []
    for data in data_list:
        try:
            validate_input(data)
            results.append(f"Processed: {data['name']}")
        except ValueError as e:
            results.append(str(e))
    return results