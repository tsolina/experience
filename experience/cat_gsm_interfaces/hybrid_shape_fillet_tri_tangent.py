from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces.hybrid_shape import HybridShape

class HybridShapeFilletTriTangent(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeFilletTriTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_fillet_tri_tangent = com

    def first_elem(self, value: Reference = None) -> Union['HybridShapeFilletTriTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.FirstElem = value._com
            return self
        return Reference(self.hybrid_shape_fillet_tri_tangent.FirstElem)

    def first_orientation(self, value: int = None) -> Union['HybridShapeFilletTriTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.FirstOrientation = value
            return self
        return self.hybrid_shape_fillet_tri_tangent.FirstOrientation

    def remove_elem(self, value: Reference = None) -> Union['HybridShapeFilletTriTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.RemoveElem = value._com
            return self
        return Reference(self.hybrid_shape_fillet_tri_tangent.RemoveElem)

    def remove_orientation(self, value: int = None) -> Union['HybridShapeFilletTriTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.RemoveOrientation = value
            return self
        return self.hybrid_shape_fillet_tri_tangent.RemoveOrientation

    def ribbon_relimitation_mode(self, value: int = None) -> Union['HybridShapeFilletTriTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode = value
            return self
        return self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode

    def second_elem(self, value: Reference = None) -> Union['HybridShapeFilletTriTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.SecondElem = value._com
            return self
        return Reference(self.hybrid_shape_fillet_tri_tangent.SecondElem)

    def second_orientation(self, value: int = None) -> Union['HybridShapeFilletTriTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.SecondOrientation = value
            return self
        return self.hybrid_shape_fillet_tri_tangent.SecondOrientation

    def supports_trim_mode(self, value: int = None) -> Union['HybridShapeFilletTriTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode = value
            return self
        return self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode

    def invert_first_orientation(self) -> 'HybridShapeFilletTriTangent':
        self.hybrid_shape_fillet_tri_tangent.InvertFirstOrientation()
        return self

    def invert_remove_orientation(self) -> 'HybridShapeFilletTriTangent':
        self.hybrid_shape_fillet_tri_tangent.InvertRemoveOrientation()
        return self

    def invert_second_orientation(self) -> 'HybridShapeFilletTriTangent':
        self.hybrid_shape_fillet_tri_tangent.InvertSecondOrientation()
        return self

    def __repr__(self):
        return f'HybridShapeFilletTriTangent(name="{ self.name }")'