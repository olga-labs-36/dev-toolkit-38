import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

    def update(self, new_config):
        self.config.update(new_config)

config_loader = ConfigLoader('default_config.json')
