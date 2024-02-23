from experience.mecmod_interfaces import Shape

class DressUpShape(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         DressUpShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.dress_up_shape = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'