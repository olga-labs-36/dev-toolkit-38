def divide_numbers(numerator, denominator):
    if not isinstance(numerator, (int, float)):
        raise ValueError('Numerator must be a number')
    if not isinstance(denominator, (int, float)):
        raise ValueError('Denominator must be a number')
    if denominator == 0:
        raise ZeroDivisionError('Denominator cannot be zero')
    return numerator / denominator


def parse_integer(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError('Invalid integer value')


def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('File not found: ' + file_path)
    except Exception as e:
        raise Exception('Error opening file: ' + str(e))


def safe_list_index(lst, index):
    if not isinstance(lst, list):
        raise ValueError('Expected a list')
    if not isinstance(index, int):
        raise ValueError('Index must be an integer')
    if index < 0 or index >= len(lst):
        raise IndexError('Index out of range')
    return lst[index]