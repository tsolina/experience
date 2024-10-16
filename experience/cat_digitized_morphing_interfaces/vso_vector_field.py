from experience.system import AnyObject

class VSOVectorField(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSOVectorField
    """

    def __init__(self, com):
        super().__init__(com)
        self.vso_vector_field = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'