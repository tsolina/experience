from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length

class HybridShapeExtrude(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtrude
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_extrude = com

    def begin_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_extrude.BeginOffset)

    def context(self, value: int = None) -> Union['HybridShapeExtrude', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.Context = value
            return self
        return self.hybrid_shape_extrude.Context

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeExtrude', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_extrude.Direction)

    def end_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_extrude.EndOffset)

    def extruded_object(self, value: Reference = None) -> Union['HybridShapeExtrude', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.ExtrudedObject = value._com
            return self
        return Reference(self.hybrid_shape_extrude.ExtrudedObject)

    def first_limit_type(self, value: int = None) -> Union['HybridShapeExtrude', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.FirstLimitType = value
            return self
        return self.hybrid_shape_extrude.FirstLimitType

    def first_upto_element(self, value: Reference = None) -> Union['HybridShapeExtrude', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.FirstUptoElement = value._com
            return self
        return Reference(self.hybrid_shape_extrude.FirstUptoElement)

    def orientation(self, value: bool = None) -> Union['HybridShapeExtrude', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.Orientation = value
            return self
        return self.hybrid_shape_extrude.Orientation

    def second_limit_type(self, value: int = None) -> Union['HybridShapeExtrude', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.SecondLimitType = value
            return self
        return self.hybrid_shape_extrude.SecondLimitType

    def second_upto_element(self, value: Reference = None) -> Union['HybridShapeExtrude', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.SecondUptoElement = value._com
            return self
        return Reference(self.hybrid_shape_extrude.SecondUptoElement)

    def symmetrical_extension(self, value: bool = None) -> Union['HybridShapeExtrude', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_extrude.SymmetricalExtension = value
            return self
        return self.hybrid_shape_extrude.SymmetricalExtension

    def __repr__(self):
        return f'HybridShapeExtrude(name="{self.name}")'