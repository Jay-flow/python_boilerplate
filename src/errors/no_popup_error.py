class NoPopupError(Exception):
    def __init__(self, message="I can't find the pop-up."):
        super().__init__(message)
