from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Point
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class HybridShapePointBetween(Point):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointBetween
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_point_between = com

    def first_point(self, value: Reference = None) -> Union['HybridShapePointBetween', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_between.FirstPoint = value._com
            return self
        return Reference(self.hybrid_shape_point_between.FirstPoint)

    def orientation(self, value: int = None) -> Union['HybridShapePointBetween', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_between.Orientation = value
            return self
        return self.hybrid_shape_point_between.Orientation

    def ratio(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_point_between.Ratio)

    def second_point(self, value: Reference = None) -> Union['HybridShapePointBetween', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_between.SecondPoint = value._com
            return self
        return Reference(self.hybrid_shape_point_between.SecondPoint)

    def support(self, value: Reference = None) -> Union['HybridShapePointBetween', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_point_between.SecondPoint = value._com
            return self
        return Reference(self.hybrid_shape_point_between.Support)

    def __repr__(self):
        return f'HybridShapePointBetween(name="{self.name}")'