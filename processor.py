import json

class Processor:
    def process_data(self, data):
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary.")
        try:
            result = self._perform_calculation(data)
            return json.dumps(result)
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero.")
        except KeyError as e:
            raise ValueError(f"Missing key: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

    def _perform_calculation(self, data):
        if 'numerator' not in data or 'denominator' not in data:
            raise KeyError('numerator or denominator')
        num = data['numerator']
        denom = data['denominator']
        return {'result': num / denom}