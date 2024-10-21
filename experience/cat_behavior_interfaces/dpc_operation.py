from experience.system import AnyObject

class DPCOperation(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DPCOperation
    """

    def __init__(self, com):
        super().__init__(com)
        self.dpc_operation = com
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'