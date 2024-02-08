from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeExtremum(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtremum
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extremum = com

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeExtremum', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction)

    def direction2(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeExtremum', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.Direction2 = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction2)

    def direction3(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeExtremum', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.Direction3 = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction3)

    def extremum_type(self, value: int = None) -> Union['HybridShapeExtremum', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.ExtremumType = value
            return self
        return self.hybrid_shape_extremum.ExtremumType

    def extremum_type2(self, value: int = None) -> Union['HybridShapeExtremum', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.ExtremumType2 = value
            return self
        return self.hybrid_shape_extremum.ExtremumType2

    def extremum_type3(self, value: int = None) -> Union['HybridShapeExtremum', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.ExtremumType3 = value
            return self
        return self.hybrid_shape_extremum.ExtremumType3

    def reference_element(self, value: Reference = None) -> Union['HybridShapeExtremum', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extremum.ReferenceElement = value._com
            return self
        return Reference(self.hybrid_shape_extremum.ReferenceElement)

    def __repr__(self):
        return f'HybridShapeExtremum(name="{ self.name }")'