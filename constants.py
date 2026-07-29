class ErrorCodes:
    INVALID_INPUT = '001'
    NOT_FOUND = '002'
    SERVER_ERROR = '003'

class Messages:
    INPUT_ERROR_MSG = 'Invalid input provided'
    NOT_FOUND_MSG = 'Requested resource not found'
    SERVER_ERROR_MSG = 'Internal server error occurred'

class Config:
    MAX_RETRIES = 3
    TIMEOUT = 5

class HTTPStatus:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

