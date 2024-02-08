from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces.length import Length

class HybridShapeCircleCenterAxis(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCenterAxis
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_center_axis = com

    def axis(self, value: Reference = None) -> Union['HybridShapeCircleCenterAxis', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_axis.Axis = value._com
            return self
        return Reference(self.hybrid_shape_circle_center_axis.Axis)

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.hybrid_shape_circle_center_axis.Diameter)

    def diameter_mode(self, value: bool = None) -> Union['HybridShapeCircleCenterAxis', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_axis.DiameterMode = value
            return self
        return self.hybrid_shape_circle_center_axis.DiameterMode

    def point(self, value: Reference = None) -> Union['HybridShapeCircleCenterAxis', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_axis.Point = value._com
            return self
        return Reference(self.hybrid_shape_circle_center_axis.Point)

    def projection_mode(self, value: bool = None) -> Union['HybridShapeCircleCenterAxis', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_center_axis.ProjectionMode = value
            return self
        return self.hybrid_shape_circle_center_axis.ProjectionMode

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.hybrid_shape_circle_center_axis.Radius)

    def __repr__(self):
        return f'HybridShapeCircleCenterAxis(name="{self.name}")'