class CutomError(Exception):
    def __init__(self, message="Custom error message."):
        super().__init__(message)
