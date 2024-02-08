from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class HybridShapeScaling(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeScaling
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_scaling = com

    def center(self, value: Reference = None) -> Union['HybridShapeScaling', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_scaling.Center = value._com
            return self
        return Reference(self.hybrid_shape_scaling.Center)

    def creation_mode(self, value: bool = None) -> Union['HybridShapeScaling', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_scaling.CreationMode = value
            return self
        return self.hybrid_shape_scaling.CreationMode

    def elem_to_scale(self, value: Reference = None) -> Union['HybridShapeScaling', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_scaling.Center = value._com
            return self
        return Reference(self.hybrid_shape_scaling.ElemToScale)

    def ratio(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_scaling.Ratio)

    def ratio_value(self, value: float = None) -> Union['HybridShapeScaling', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_scaling.RatioValue = value
            return self
        return self.hybrid_shape_scaling.RatioValue

    def volume_result(self, value: bool = None) -> Union['HybridShapeScaling', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_scaling.VolumeResult = value
            return self
        return self.hybrid_shape_scaling.VolumeResult

    def __repr__(self):
        return f'HybridShapeScaling(name="{self.name}")'