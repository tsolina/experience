from experience.system import AnyObject
from experience.cat_sketcher_interfaces.sketcher_types import *

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

    def geometric_type(self) -> CatGeometricType:
        return CatGeometricType.item(self.geometric_element.GeometricType)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'