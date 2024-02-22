from experience.system import AnyObject

class Workbench(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Workbench
    """
    def __init__(self, com):
        super().__init__(com)
        self.workbench = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'