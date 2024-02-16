from experience.system import AnyObject

class Shape(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Shape
    """

    def __init__(self, com):
        super().__init__(com)
        self.shape = com

    def __repr__(self):
        return f'Shape(name="{self.name()}")'