"""### Exceptions used by the module."""

class RequestError(Exception):
    """### Error raised when an HTTP request failed"""
    def __init__(self, message = None):
        self.message = message
        super().__init__(self.message)