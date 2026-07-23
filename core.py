from typing import Any, Dict

class Configuration:
    def __init__(self, config_data: Dict[str, Any]) -> None:
        """Initialize configuration with given data."""
        self.config_data = config_data

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for the given key or default if key not found."""
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set the value for the given key."""
        self.config_data[key] = value

    def remove(self, key: str) -> None:
        """Remove the key from the configuration, if present."""
        self.config_data.pop(key, None)

    def items(self) -> Dict[str, Any]:
        """Return all configuration items as a dictionary."""
        return self.config_data.items()

    def clear(self) -> None:
        """Clear all configuration data."""
        self.config_data.clear()

if __name__ == '__main__':
    config = Configuration({'host': 'localhost', 'port': 8080})
    print(config.get('host'))
    config.set('debug', True)
    print(config.items())
    config.remove('port')
    print(config.items())