from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class HybridShapeAffinity(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAffinity
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_affinity = com

    def axis_first_direction(self, value: Reference = None) -> Union['HybridShapeAffinity', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.AxisFirstDirection = value._com
            return self
        return Reference(self.hybrid_shape_affinity.AxisFirstDirection)

    def axis_origin(self, value: Reference = None) -> Union['HybridShapeAffinity', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.AxisOrigin = value._com
            return self
        return Reference(self.hybrid_shape_affinity.AxisOrigin)

    def axis_plane(self, value: Reference = None) -> Union['HybridShapeAffinity', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.AxisPlane = value._com
            return self
        return Reference(self.hybrid_shape_affinity.AxisPlane)

    def creation_mode(self, value: bool = None) -> Union['HybridShapeAffinity', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.CreationMode = value
            return self
        return self.hybrid_shape_affinity.CreationMode

    def elem_to_transform(self, value: Reference = None) -> Union['HybridShapeAffinity', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.ElemToTransform = value._com
            return self
        return Reference(self.hybrid_shape_affinity.ElemToTransform)

    def volume_result(self, value: bool = None) -> Union['HybridShapeAffinity', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_affinity.VolumeResult = value
            return self
        return self.hybrid_shape_affinity.VolumeResult

    def x_ratios(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_affinity.XRatios)

    def y_ratios(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_affinity.YRatios)

    def z_ratios(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_affinity.ZRatios)

    def __repr__(self):
        return f'HybridShapeAffinity(name="{self.name}")'