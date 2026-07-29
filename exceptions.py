class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Not found"): 
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    def __init__(self, message="Invalid input"): 
        self.message = message
        super().__init__(self.message)

class DatabaseError(CustomError):
    def __init__(self, message="Database error occurred"): 
        self.message = message
        super().__init__(self.message)