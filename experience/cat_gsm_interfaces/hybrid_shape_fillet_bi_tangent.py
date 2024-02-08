from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeIntegratedLaw
    from experience.knowledge_interfaces import Length

class HybridShapeFilletBiTangent(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeFilletBiTangent
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_fillet_bi_tangent = com

    def conical_section_parameter(self, value: float = None) -> Union['HybridShapeFilletBiTangent', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter

    def first_elem(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.FirstElem = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstElem)

    def first_law_relimiter(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter)

    def first_orientation(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.FirstOrientation = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.FirstOrientation

    def hold_curve(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.HoldCurve = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.HoldCurve)

    def integrated_law(self, value: 'HybridShapeIntegratedLaw' = None) -> Union['HybridShapeFilletBiTangent', 'HybridShapeIntegratedLaw']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.IntegratedLaw = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeIntegratedLaw
        return HybridShapeIntegratedLaw(self.hybrid_shape_fillet_bi_tangent.IntegratedLaw)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_fillet_bi_tangent.Radius)

    def radius_type(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.RadiusType = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.RadiusType

    def radius_value(self, value: float = None) -> Union['HybridShapeFilletBiTangent', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.RadiusValue = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.RadiusValue

    def ribbon_relimitation_mode(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode

    def second_elem(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.SecondElem = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondElem)

    def second_law_relimiter(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter)

    def second_orientation(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.SecondOrientation = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.SecondOrientation

    def section_type(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.SectionType = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.SectionType

    def spine(self, value: Reference = None) -> Union['HybridShapeFilletBiTangent', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.Spine = value._com
            return self
        return Reference(self.hybrid_shape_fillet_bi_tangent.Spine)

    def supports_trim_mode(self, value: int = None) -> Union['HybridShapeFilletBiTangent', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode = value
            return self
        return self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode

    def append_new_face_to_keep(self, i_face: Reference) -> 'HybridShapeFilletBiTangent':
        self.hybrid_shape_fillet_bi_tangent.AppendNewFaceToKeep(i_face._com)
        return self

    def get_face_to_keep(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.GetFaceToKeep(i_pos))

    def invert_first_orientation(self) -> 'HybridShapeFilletBiTangent':
        self.hybrid_shape_fillet_bi_tangent.InvertFirstOrientation()
        return self

    def invert_second_orientation(self) -> 'HybridShapeFilletBiTangent':
        self.hybrid_shape_fillet_bi_tangent.InvertSecondOrientation()
        return self

    def remove_all_faces_to_keep(self) -> 'HybridShapeFilletBiTangent':
        self.hybrid_shape_fillet_bi_tangent.RemoveAllFacesToKeep()
        return self

    def remove_face_to_keep(self, i_face: Reference) -> 'HybridShapeFilletBiTangent':
        self.hybrid_shape_fillet_bi_tangent.RemoveFaceToKeep(i_face._com)
        return self

    def __repr__(self):
        return f'HybridShapeFilletBiTangent(name="{self.name}")'