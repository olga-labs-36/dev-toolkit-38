import os

class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.db_url = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
        self.debug = self.environment == 'development'

    def get_db_url(self):
        return self.db_url

    def is_debug_mode(self):
        return self.debug

config = Config()