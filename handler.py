import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def update_json(file_path, updates):
    data = load_json(file_path)
    data.update(updates)
    save_json(data, file_path)


def get_value(data, key, default=None):
    return data.get(key, default)


def set_value(data, key, value):
    data[key] = value


def delete_key(data, key):
    if key in data:
        del data[key]