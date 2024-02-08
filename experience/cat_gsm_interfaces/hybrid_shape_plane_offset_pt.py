from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlaneOffsetPt(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneOffsetPt
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_offset_pt = com

    def ref_plane(self, value: Reference = None) -> Union['HybridShapePlaneOffsetPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_offset_pt.Plane = value._com
            return self
        return Reference(self.hybrid_shape_plane_offset_pt.Plane)

    def point(self, value: Reference = None) -> Union['HybridShapePlaneOffsetPt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane_offset_pt.Point = value._com
            return self
        return Reference(self.hybrid_shape_plane_offset_pt.Point)

    def __repr__(self):
        return f'HybridShapePlaneOffsetPt(name="{self.name}")'