from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlane1Line1Pt(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane1Line1Pt
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane1_line1_pt = com

    def line(self, value: Reference = None) -> Union['HybridShapePlane1Line1Pt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane1_line1_pt.Line = value._com
            return self
        return Reference(self.hybrid_shape_plane1_line1_pt.Line)

    def point(self, value: Reference = None) -> Union['HybridShapePlane1Line1Pt', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane1_line1_pt.Point = value._com
            return self
        return Reference(self.hybrid_shape_plane1_line1_pt.Point)

    def __repr__(self):
        return f'HybridShapePlane1Line1Pt(name="{self.name}")'