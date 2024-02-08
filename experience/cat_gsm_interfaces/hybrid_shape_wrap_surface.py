from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeWrapSurface(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeWrapSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_wrap_surface = com

    def deformation_mode(self, value: int = None) -> Union['HybridShapeWrapSurface', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_surface.DeformationMode = value
            return self
        return self.hybrid_shape_wrap_surface.DeformationMode

    def reference_surface(self, value: Reference = None) -> Union['HybridShapeWrapSurface', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_surface.ReferenceSurface = value._com
            return self
        return Reference(self.hybrid_shape_wrap_surface.ReferenceSurface)

    def surface(self, value: Reference = None) -> Union['HybridShapeWrapSurface', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_surface.Surface = value._com
            return self
        return Reference(self.hybrid_shape_wrap_surface.Surface)

    def target_surface(self) -> Reference:
        return Reference(self.hybrid_shape_wrap_surface.TargetSurface)

    def __repr__(self):
        return f'HybridShapeWrapSurface(name="{self.name}")'