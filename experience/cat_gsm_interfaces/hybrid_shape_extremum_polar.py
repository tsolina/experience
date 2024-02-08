from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeExtremumPolar(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtremumPolar
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extremum_polar = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_extremum_polar.Angle)

    def contour(self, value: Reference = None) -> Union['HybridShapeExtremumPolar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum_polar.Contour = value._com
            return self
        return Reference(self.hybrid_shape_extremum_polar.Contour)

    def dir(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeExtremumPolar', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum_polar.Dir = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_extremum_polar.Dir)

    def extremum_type(self, value: int = None) -> Union['HybridShapeExtremumPolar', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum_polar.ExtremumType = value
            return self
        return self.hybrid_shape_extremum_polar.ExtremumType

    def origin(self, value: Reference = None) -> Union['HybridShapeExtremumPolar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum_polar.Origin = value._com
            return self
        return Reference(self.hybrid_shape_extremum_polar.Origin)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_extremum_polar.Radius)

    def support(self, value: Reference = None) -> Union['HybridShapeExtremumPolar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum_polar.Support = value._com
            return self
        return Reference(self.hybrid_shape_extremum_polar.Support)

    def __repr__(self):
        return f'HybridShapeExtremumPolar(name="{ self.name }")'