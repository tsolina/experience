from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeBoundary(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeBoundary
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_boundary = com

    def from_(self, value: Reference = None) -> Union['HybridShapeBoundary', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.From = value._com
            return self
        return Reference(self.hybrid_shape_boundary.From)

    def from_orientation(self, value: int = None) -> Union['HybridShapeBoundary', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.FromOrientation = value
            return self
        return self.hybrid_shape_boundary.FromOrientation

    def initial_element(self, value: Reference = None) -> Union['HybridShapeBoundary', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.InitialElement = value._com
            return self
        return Reference(self.hybrid_shape_boundary.InitialElement)

    def propagation(self, value: int = None) -> Union['HybridShapeBoundary', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.Propagation = value
            return self
        return self.hybrid_shape_boundary.Propagation

    def support(self, value: Reference = None) -> Union['HybridShapeBoundary', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.Support = value._com
            return self
        return Reference(self.hybrid_shape_boundary.Support)

    def to(self, value: Reference = None) -> Union['HybridShapeBoundary', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.To = value._com
            return self
        return Reference(self.hybrid_shape_boundary.To)

    def to_orientation(self, value: int = None) -> Union['HybridShapeBoundary', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_boundary.ToOrientation = value
            return self
        return self.hybrid_shape_boundary.ToOrientation

    def __repr__(self):
        return f'HybridShapeBoundary(name="{self.name}")'