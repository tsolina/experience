from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import Length
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShape3DCurveOffset(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShape3DCurveOffset
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_3d_curve_offset = com

    def corner_radius_value(self, value: Length = None) -> Union['HybridShape3DCurveOffset', Length]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.CornerRadiusValue = value._com
            return self
        return Length(self.hybrid_shape_3d_curve_offset.CornerRadiusValue)

    def corner_tension_value(self, value: float = None) -> Union['HybridShape3DCurveOffset', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.CornerTensionValue = value
            return self
        return self.hybrid_shape_3d_curve_offset.CornerTensionValue

    def curve_to_offset(self, value: Reference = None) -> Union['HybridShape3DCurveOffset', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.CurveToOffset = value._com
            return self
        return Reference(self.hybrid_shape_3d_curve_offset.CurveToOffset)

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShape3DCurveOffset', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_3d_curve_offset.Direction)

    def invert_direction(self, value: bool = None) -> Union['HybridShape3DCurveOffset', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.InvertDirection = value._com
            return self
        return self.hybrid_shape_3d_curve_offset.InvertDirection

    def offset_value(self, value: Length = None) -> Union['HybridShape3DCurveOffset', Length]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_3d_curve_offset.OffsetValue = value._com
            return self
        return Length(self.hybrid_shape_3d_curve_offset.OffsetValue)

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{self.name}")'