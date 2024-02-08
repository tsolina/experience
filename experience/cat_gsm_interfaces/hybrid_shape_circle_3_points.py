from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

class HybridShapeCircle3Points(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircle3Points
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle3_points = com

    def element1(self, value: Reference = None) -> Union['HybridShapeCircle3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle3_points.Element1 = value._com
            return self
        return Reference(self.hybrid_shape_circle3_points.Element1)

    def element2(self, value: Reference = None) -> Union['HybridShapeCircle3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle3_points.Element2 = value._com
            return self
        return Reference(self.hybrid_shape_circle3_points.Element2)

    def element3(self, value: Reference = None) -> Union['HybridShapeCircle3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle3_points.Element3 = value._com
            return self
        return Reference(self.hybrid_shape_circle3_points.Element3)

    def support(self, value: Reference = None) -> Union['HybridShapeCircle3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle3_points.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle3_points.Support)

    def remove_support(self) -> 'HybridShapeCircle3Points':
        """ perform the action and return self"""
        self.hybrid_shape_circle3_points.RemoveSupport()
        return self

    def __repr__(self):
        return f'HybridShapeCircle3Points(name="{self.name}")'