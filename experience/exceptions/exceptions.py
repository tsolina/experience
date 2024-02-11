class CATIABaseException(Exception):
    """
    CATIABaseException class.
    """
    pass


class CATIAApplicationException(CATIABaseException):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'CATIAApplicationException()'
