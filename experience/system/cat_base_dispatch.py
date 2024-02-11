from experience.system import CATBaseUnknown

class CATBaseDispatch(CATBaseUnknown):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             CATBaseDispatch
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'CatBaseDispatch()'
