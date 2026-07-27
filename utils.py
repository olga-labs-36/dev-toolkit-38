import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def filter_dict(data_dict, filter_func):
    return {k: v for k, v in data_dict.items() if filter_func(k, v)}
