from experience.system.i_dispatch import IDispatch

class CATBaseUnknown(IDispatch):
    """
                | System.IUnknown
                |     System.IDispatch
                |         CATBaseUnknown
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'CatBaseUnknown()'
