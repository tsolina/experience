from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape


class HybridShapeAxisToAxis(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAxisToAxis
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_axis_to_axis = com

    def creation_mode(self, value: bool = None) -> Union['HybridShapeAxisToAxis', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_to_axis.CreationMode = value
            return self
        return self.hybrid_shape_axis_to_axis.CreationMode

    def elem_to_transform(self, value: Reference = None) -> Union['HybridShapeAxisToAxis', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_to_axis.ElemToTransform = value._com
            return self
        return Reference(self.hybrid_shape_axis_to_axis.ElemToTransform)

    def reference_axis(self, value: Reference = None) -> Union['HybridShapeAxisToAxis', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_to_axis.ReferenceAxis = value._com
            return self
        return Reference(self.hybrid_shape_axis_to_axis.ReferenceAxis)

    def target_axis(self, value: Reference = None) -> Union['HybridShapeAxisToAxis', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_to_axis.TargetAxis = value._com
            return self
        return Reference(self.hybrid_shape_axis_to_axis.TargetAxis)

    def volume_result(self, value: bool = None) -> Union['HybridShapeAxisToAxis', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_to_axis.VolumeResult = value
            return self
        return self.hybrid_shape_axis_to_axis.VolumeResult

    def __repr__(self):
        return f'HybridShapeAxisToAxis(name="{self.name}")'