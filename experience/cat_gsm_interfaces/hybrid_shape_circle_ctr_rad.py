from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeCircle
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeCircleCtrRad(HybridShapeCircle):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCtrRad
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_circle_ctr_rad = com

    def center(self, value: Reference = None) -> Union['HybridShapeCircleCtrRad', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_rad.Center = value._com
            return self
        return Reference(self.hybrid_shape_circle_ctr_rad.Center)

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_ctr_rad.Diameter)

    def diameter_mode(self, value: bool = None) -> Union['HybridShapeCircleCtrRad', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_rad.DiameterMode = value
            return self
        return self.hybrid_shape_circle_ctr_rad.DiameterMode

    def first_direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCircleCtrRad', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_rad.FirstDirection = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_circle_ctr_rad.FirstDirection)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_circle_ctr_rad.Radius)

    def support(self, value: Reference = None) -> Union['HybridShapeCircleCtrRad', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_circle_ctr_rad.Support = value._com
            return self
        return Reference(self.hybrid_shape_circle_ctr_rad.Support)

    def get_second_direction(self) -> tuple[float, float, float]:
        return self.hybrid_shape_circle_ctr_rad.GetSecondDirection()

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle_ctr_rad.IsGeodesic()

    def set_geometry_on_support(self) -> 'HybridShapeCircleCtrRad':
        """ perform the action and return self"""
        self.hybrid_shape_circle_ctr_rad.SetGeometryOnSupport()
        return self

    def set_second_direction(self, i_dir_x: float, i_dir_y: float, i_dir_z: float) -> 'HybridShapeCircleCtrRad':
        """ perform the action and return self"""
        self.hybrid_shape_circle_ctr_rad.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)
        return self

    def unset_geometry_on_support(self) -> 'HybridShapeCircleCtrRad':
        """ perform the action and return self"""
        self.hybrid_shape_circle_ctr_rad.UnsetGeometryOnSupport()
        return self

    def __repr__(self):
        return f'HybridShapeCircleCtrRad(name="{ self.name }")'