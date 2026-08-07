class Constants:
    MAX_USERS = 1000
    MIN_USERS = 1
    DEFAULT_TIMEOUT = 30
    API_URL = 'https://api.example.com'
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'

    @classmethod
    def get_statuses(cls):
        return [cls.STATUS_ACTIVE, cls.STATUS_INACTIVE]

    @classmethod
    def get_user_limits(cls):
        return (cls.MIN_USERS, cls.MAX_USERS)

    @classmethod
    def get_api_url(cls):
        return cls.API_URL

    @classmethod
    def get_timeout(cls):
        return cls.DEFAULT_TIMEOUT

    @staticmethod
    def is_status_valid(status):
        return status in [Constants.STATUS_ACTIVE, Constants.STATUS_INACTIVE]