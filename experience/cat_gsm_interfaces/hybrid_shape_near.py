from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeNear(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeNear
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_near = com

    def multiple_solution(self, value: Reference = None) -> Union['HybridShapeNear', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_near.MultipleSolution = value._com
            return self
        return Reference(self.hybrid_shape_near.MultipleSolution)

    def reference_element(self, value: Reference = None) -> Union['HybridShapeNear', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_near.ReferenceElement = value._com
            return self
        return Reference(self.hybrid_shape_near.ReferenceElement)

    def __repr__(self):
        return f'HybridShapeNear(name="{ self.name }")'