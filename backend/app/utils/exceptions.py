class AppError(Exception):
    message = "Application error"


class NotFoundError(AppError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ConflictError(AppError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class AuthenticationError(AppError):
    def __init__(self, message: str = "Authentication failed"):
        self.message = message
        super().__init__(message)
