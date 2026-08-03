def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def list_to_dict(lst, key):
    return {getattr(item, key): item for item in lst}


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def dict_to_list(d):
    return [{'key': k, 'value': v} for k, v in d.items()]


def is_empty(value):
    return value is None or value == ''