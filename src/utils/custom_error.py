class CutomError(Exception):
    def __init__(self, message="Custom error message."):
        super().__init__(message)


class NoPopupError(Exception):
    def __init__(self, message="I can't find the pop-up."):
        super().__init__(message)
