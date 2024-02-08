from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlaneTangent(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_tangent = com

    def point(self, value: Reference = None) -> Union['HybridShapePlaneTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_tangent.Point = value._com
            return self
        return Reference(self.hybrid_shape_plane_tangent.Point)

    def surface(self, value: Reference = None) -> Union['HybridShapePlaneTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_tangent.Surface = value._com
            return self
        return Reference(self.hybrid_shape_plane_tangent.Surface)

    def __repr__(self):
        return f'HybridShapePlaneTangent(name="{self.name}")'