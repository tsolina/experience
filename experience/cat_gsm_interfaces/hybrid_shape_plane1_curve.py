from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlane1Curve(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane1Curve
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane1_curve = com

    def curve(self, value: Reference = None) -> Union['HybridShapePlane1Curve', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane1_curve.Curve = value._com
            return self
        return Reference(self.hybrid_shape_plane1_curve.Curve)

    def __repr__(self):
        return f'HybridShapePlane1Curve(name="{self.name}")'