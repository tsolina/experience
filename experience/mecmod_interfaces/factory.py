from experience.system import AnyObject

class Factory(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Factory
    """

    def __init__(self, com):
        super().__init__(com)
        self.factory = com