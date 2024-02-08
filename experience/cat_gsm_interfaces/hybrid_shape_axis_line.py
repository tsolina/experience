from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeAxisLine(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAxisLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_axis_line = com

    def axis_line_type(self, value: int = None) -> Union['HybridShapeAxisLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_line.AxisLineType = value
            return self
        return self.hybrid_shape_axis_line.AxisLineType

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeAxisLine', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_line.Direction = value
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_axis_line.Direction)

    @property
    def element(self, value: Reference = None) -> Union['HybridShapeAxisLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_axis_line.Element = value
            return self
        return Reference(self.hybrid_shape_axis_line.Element)

    def __repr__(self):
        return f'HybridShapeAxisLine(name="{ self.name }")'