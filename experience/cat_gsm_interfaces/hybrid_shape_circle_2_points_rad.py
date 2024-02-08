from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_gsm_interfaces import HybridShapeCircle

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    
class HybridShapeCircle2PointsRad(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircle2PointsRad
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle2_points_rad = com

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle2_points_rad.Diameter)

    def diameter_mode(self, value: bool = None) -> Union['HybridShapeCircle2PointsRad', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle2_points_rad.DiameterMode = value
            return self
        return self.hybrid_shape_circle2_points_rad.DiameterMode

    def orientation(self, value: int = None) -> Union['HybridShapeCircle2PointsRad', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle2_points_rad.Orientation = value
            return self
        return self.hybrid_shape_circle2_points_rad.Orientation

    def pt1(self, value: Reference = None) -> Union['HybridShapeCircle2PointsRad', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle2_points_rad.Pt1 = value._com
            return self
        return Reference(self.hybrid_shape_circle2_points_rad.Pt1)

    def pt2(self, value: Reference = None) -> Union['HybridShapeCircle2PointsRad', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle2_points_rad.Pt1 = value._com
            return self
        return Reference(self.hybrid_shape_circle2_points_rad.Pt2)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle2_points_rad.Radius)

    def support(self, value: Reference = None) -> Union['HybridShapeCircle2PointsRad', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle2_points_rad.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle2_points_rad.Support)

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle2_points_rad.IsGeodesic()

    def set_geometry_on_support(self) -> 'HybridShapeCircle2PointsRad':
        self.hybrid_shape_circle2_points_rad.SetGeometryOnSupport()
        return self

    def unset_geometry_on_support(self) -> 'HybridShapeCircle2PointsRad':
        self.hybrid_shape_circle2_points_rad.UnsetGeometryOnSupport()
        return self

    def __repr__(self):
        return f'HybridShapeCircle2PointsRad(name="{self.name}")'