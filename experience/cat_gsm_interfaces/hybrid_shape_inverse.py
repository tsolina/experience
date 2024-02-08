from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeInverse(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeInverse
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_inverse = com

    def element(self, value: Reference = None) -> Union['HybridShapeInverse', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_inverse.Element = value._com
            return self
        return Reference(self.hybrid_shape_inverse.Element)

    def orientation(self, value: int = None) -> Union['HybridShapeInverse', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_inverse.Orientation = value
            return self
        return self.hybrid_shape_inverse.Orientation

    def __repr__(self):
        return f'HybridShapeInverse(name="{self.name}")'