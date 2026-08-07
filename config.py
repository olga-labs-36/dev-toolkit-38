import json
import os

class ConfigLoader:
    def __init__(self, default_config_file):
        self.default_config_file = default_config_file
        self.config = self.load_defaults()

    def load_defaults(self):
        if os.path.exists(self.default_config_file):
            with open(self.default_config_file, 'r') as f:
                return json.load(f)
        return {}

    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self, config_file):
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=4)