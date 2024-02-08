from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces.point import Point
from experience.inf_interfaces.reference import Reference

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces.hybrid_shape_direction import HybridShapeDirection

class HybridShapePointTangent(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_tangent = com

    def curve(self, value: Reference = None) -> Union['HybridShapePointTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_tangent.Curve = value._com
            return self
        return Reference(self.hybrid_shape_point_tangent.Curve)

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapePointTangent', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_tangent.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_point_tangent.Direction)

    def __repr__(self):
        return f'HybridShapePointTangent(name="{self.name}")'