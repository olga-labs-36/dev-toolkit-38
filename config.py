import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_config(self, file_path):
        try:
            with open(file_path, 'r') as f:
                file_config = json.load(f)
            self.config.update(file_config)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def all(self):
        return self.config

# Example default configuration
DEFAULT_CONFIG = {
    'setting1': 'default_value1',
    'setting2': 10,
    'setting3': True,
}

# Usage
config_loader = ConfigLoader(DEFAULT_CONFIG)
config_loader.load_config('config.json')
print(config_loader.all())