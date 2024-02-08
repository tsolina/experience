from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlaneNormal(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneNormal
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_normal = com

    def curve(self, value: Reference = None) -> Union['HybridShapePlaneNormal', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_normal.Curve = value._com
            return self
        return Reference(self.hybrid_shape_plane_normal.Curve)

    def point(self, value: Reference = None) -> Union['HybridShapePlaneNormal', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_normal.Point = value._com
            return self
        return Reference(self.hybrid_shape_plane_normal.Point)

    def __repr__(self):
        return f'HybridShapePlaneNormal(name="{self.name}")'