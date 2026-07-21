import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        try:
            self.validate_data()
            result = self.perform_calculation()
            return json.dumps(result)
        except ValueError as e:
            return json.dumps({'error': str(e)})
        except TypeError as e:
            return json.dumps({'error': 'Invalid data type: ' + str(e)})
        except Exception as e:
            return json.dumps({'error': 'An unexpected error occurred: ' + str(e)})

    def validate_data(self):
        if not isinstance(self.data, list):
            raise ValueError('Data must be a list.')
        if not all(isinstance(i, (int, float)) for i in self.data):
            raise ValueError('All elements must be numbers.')

    def perform_calculation(self):
        return {
            'sum': sum(self.data),
            'average': sum(self.data) / len(self.data) if self.data else 0
        }
