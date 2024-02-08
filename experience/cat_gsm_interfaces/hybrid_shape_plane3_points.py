from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlane3Points(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane3Points
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane3_points = com

    def first(self, value: Reference = None) -> Union['HybridShapePlane3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane3_points.First = value._com
            return self
        return Reference(self.hybrid_shape_plane3_points.First)

    def second(self, value: Reference = None) -> Union['HybridShapePlane3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane3_points.Second = value._com
            return self
        return Reference(self.hybrid_shape_plane3_points.Second)

    def third(self, value: Reference = None) -> Union['HybridShapePlane3Points', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane3_points.Third = value._com
            return self
        return Reference(self.hybrid_shape_plane3_points.Third)

    def __repr__(self):
        return f'HybridShapePlane3Points(name="{self.name}")'