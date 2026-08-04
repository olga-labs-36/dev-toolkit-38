from typing import Any, Dict

class Config:
    """Configuration manager for application settings."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value by key."""
        self.settings[key] = value

    def all(self) -> Dict[str, Any]:
        """Return all configuration settings."""
        return self.settings

# Example usage
if __name__ == '__main__':
    config = Config({'debug': True, 'port': 8080})
    print(config.get('debug'))
    config.set('port', 9090)
    print(config.all())