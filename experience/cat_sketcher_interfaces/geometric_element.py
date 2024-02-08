from experience.system import AnyObject

class GeometricElement(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     GeometricElement
    """

    def __init__(self, com):
        super().__init__(com)
        self.geometric_element = com

    def geometric_type(self) -> int:
        return self.geometric_element.GeometricType

    def __repr__(self):
        return f'GeometricElement(name="{self.name}")'
