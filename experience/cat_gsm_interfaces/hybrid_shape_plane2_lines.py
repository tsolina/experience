from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlane2Lines(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane2Lines
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane2_lines = com

    def first(self, value: Reference = None) -> Union['HybridShapePlane2Lines', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane2_lines.First = value._com
            return self
        return Reference(self.hybrid_shape_plane2_lines.First)

    def forbid_non_coplanar_lines(self, value: bool = None) -> Union['HybridShapePlane2Lines', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines = value
            return self
        return self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines()

    def second(self, value: Reference = None) -> Union['HybridShapePlane2Lines', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_plane2_lines.Second = value._com
            return self
        return Reference(self.hybrid_shape_plane2_lines.Second)

    def __repr__(self):
        return f'HybridShapePlane2Lines(name="{self.name}")'