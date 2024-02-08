from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length, RealParam

class HybridShapePointOnCurve(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointOnCurve
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_on_curve = com

    def curve(self, value: Reference = None) -> Union['HybridShapePointOnCurve', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.Curve = value._com
            return self
        return Reference(self.hybrid_shape_point_on_curve.Curve)

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapePointOnCurve', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_point_on_curve.Direction)

    def distance_type(self, value: int = None) -> Union['HybridShapePointOnCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.DistanceType = value
            return self
        return self.hybrid_shape_point_on_curve.DistanceType

    def offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_point_on_curve.Offset)

    def on_curve_type(self, value: int = None) -> Union['HybridShapePointOnCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.OnCurveType = value
            return self
        return self.hybrid_shape_point_on_curve.OnCurveType

    def orientation(self, value: int = None) -> Union['HybridShapePointOnCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.Orientation = value
            return self
        return self.hybrid_shape_point_on_curve.Orientation

    def point(self, value: Reference = None) -> Union['HybridShapePointOnCurve', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.Point = value._com
            return self
        return Reference(self.hybrid_shape_point_on_curve.Point)

    def ratio(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_point_on_curve.Ratio)

    def type(self, value: int = None) -> Union['HybridShapePointOnCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_on_curve.Type = value
            return self
        return self.hybrid_shape_point_on_curve.Type

    def __repr__(self):
        return f'HybridShapePointOnCurve(name="{self.name}")'