from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeMidSurface(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeMidSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_mid_surface = com

    def auto_thickness_threshold(self, value: int = None) -> Union['HybridShapeMidSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_mid_surface.AutoThicknessThreshold = value
            return self
        return self.hybrid_shape_mid_surface.AutoThicknessThreshold

    def creation_mode(self, value: int = None) -> Union['HybridShapeMidSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_mid_surface.CreationMode = value
            return self
        return self.hybrid_shape_mid_surface.CreationMode

    def support(self, value: Reference = None) -> Union['HybridShapeMidSurface', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_mid_surface.Support = value._com
            return self
        return Reference(self.hybrid_shape_mid_surface.Support)

    def threshold(self, value: 'Length' = None) -> Union['HybridShapeMidSurface', 'Length']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_mid_surface.Threshold = value._com
            return self
        return Length(self.hybrid_shape_mid_surface.Threshold)

    def __repr__(self):
        return f'HybridShapeMidSurface(name="{self.name}")'