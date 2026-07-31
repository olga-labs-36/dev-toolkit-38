import json

class CustomError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        raise CustomError('Data must be a dictionary')
    if 'id' not in data:
        raise CustomError('Missing required key: id')
    if 'value' not in data:
        raise CustomError('Missing required key: value')
    return f'Processed {data['id']} with value {data['value']}'

def handle_request(request):
    try:
        data = json.loads(request)
        result = process_data(data)
        return json.dumps({'status': 'success', 'result': result})
    except json.JSONDecodeError:
        return json.dumps({'status': 'error', 'message': 'Invalid JSON'}), 400
    except CustomError as ce:
        return json.dumps({'status': 'error', 'message': str(ce)}), 400
    except Exception as e:
        return json.dumps({'status': 'error', 'message': 'An unexpected error occurred'}), 500