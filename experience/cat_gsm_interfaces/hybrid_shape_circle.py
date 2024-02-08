from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeCircle(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCircle
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle = com

    def axis_computation(self, value: bool = None) -> Union['HybridShapeCircle', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle.AxisComputation = value
            return self
        return self.hybrid_shape_circle.AxisComputation

    def axis_direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCircle', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle.AxisDirection = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_circle.AxisDirection)

    def end_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_circle.EndAngle)

    def start_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_circle.StartAngle)

    def get_axis(self, i_position: int) -> Reference:
        ### didnt found a single example in vba where this should work ###
        return self.hybrid_shape_circle.GetAxis(i_position)

    def get_center(self) -> tuple[float, float, float]:
        return self.hybrid_shape_circle.GetCenter()

    def get_free_center(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetFreeCenter", 2)

    def get_free_radius(self) -> float:
        return self.hybrid_shape_circle.GetFreeRadius()

    def get_limitation(self) -> int:
        return self.hybrid_shape_circle.GetLimitation()

    def set_limitation(self, i_limitation: int) -> 'HybridShapeCircle':
        self.hybrid_shape_circle.SetLimitation(i_limitation)
        return self
    
    def limitation(self, value: int = None) -> Union['HybridShapeCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle.SetLimitation(value)
            return self
        return self.hybrid_shape_circle.GetLimitation()

    def __repr__(self):
        return f'HybridShapeCircle(name="{self.name}")'