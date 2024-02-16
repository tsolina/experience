from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import SurfaceBasedShape

class SewSurface(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             SewSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.sew_surface = com

    def deviation(self, value: float = None) -> Union['SewSurface', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sew_surface.Deviation = value
            return self
        return self.sew_surface.Deviation

    def deviation_mode(self, value: int = None) -> Union['SewSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sew_surface.DeviationMode = value
            return self
        return self.sew_surface.DeviationMode

    def sewing_intersection_mode(self, value: int = None) -> Union['SewSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sew_surface.SewingIntersectionMode = value
            return self
        return self.sew_surface.SewingIntersectionMode

    def sewing_side(self, value: int = None) -> Union['SewSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sew_surface.SewingSide = value
            return self
        return self.sew_surface.SewingSide

    def set_surface_support(self, i_support_surface: Reference) -> 'SewSurface':
        self.sew_surface.SetSurfaceSupport(i_support_surface._com)
        return self

    def set_volume_support(self, i_volume: Reference) -> 'SewSurface':
        self.sew_surface.SetVolumeSupport(i_volume._com)
        return self

    def __repr__(self):
        return f'SewSurface(name="{self.name()}")'