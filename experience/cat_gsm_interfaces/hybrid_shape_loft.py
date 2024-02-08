from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    # from experience.scripts.vba import vba_nothing

class HybridShapeLoft(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeLoft
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_loft = com

    def area_law(self, value: Reference = None) -> Union['HybridShapeLoft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.AreaLaw = value._com
            return self
        return Reference(self.hybrid_shape_loft.AreaLaw)

    def area_law_tolerance(self, value: float = None) -> Union['HybridShapeLoft', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.AreaLawTolerance = value
            return self
        return self.hybrid_shape_loft.AreaLawTolerance

    def boolean_operation(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.BooleanOperation = value
            return self
        return self.hybrid_shape_loft.BooleanOperation

    def canonical_detection(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.CanonicalDetection = value
            return self
        return self.hybrid_shape_loft.CanonicalDetection

    def comp_end_section_tangent(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.CompEndSectionTangent = value
            return self
        return self.hybrid_shape_loft.CompEndSectionTangent

    def comp_start_section_tangent(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.CompStartSectionTangent = value
            return self
        return self.hybrid_shape_loft.CompStartSectionTangent

    def context(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.Context = value
            return self
        return self.hybrid_shape_loft.Context

    def relimitation(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.Relimitation = value
            return self
        return self.hybrid_shape_loft.Relimitation

    def section_coupling(self, value: int = None) -> Union['HybridShapeLoft', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.SectionCoupling = value
            return self
        return self.hybrid_shape_loft.SectionCoupling

    def smooth_angle_threshold(self, value: float = None) -> Union['HybridShapeLoft', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.SmoothAngleThreshold = value
            return self
        return self.hybrid_shape_loft.SmoothAngleThreshold

    def smooth_angle_threshold_activity(self, value: bool = None) -> Union['HybridShapeLoft', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.SmoothAngleThresholdActivity = value
            return self
        return self.hybrid_shape_loft.SmoothAngleThresholdActivity

    def smooth_deviation(self, value: float = None) -> Union['HybridShapeLoft', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.SmoothDeviation = value
            return self
        return self.hybrid_shape_loft.SmoothDeviation

    def smooth_deviation_activity(self, value: bool = None) -> Union['HybridShapeLoft', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_loft.SmoothDeviationActivity = value
            return self
        return self.hybrid_shape_loft.SmoothDeviationActivity


    def add_guide(self, i_guide: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.AddGuide(i_guide._com)
        return self

    def add_guide_with_tangent(self, i_guide: Reference, i_tangent: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.AddGuideWithTangent(i_guide._com, i_tangent._com)
        return self

    def add_section_to_loft(self, i_crv: Reference, i_ori: int, i_point: Reference) -> None:
        return self.hybrid_shape_loft.AddSectionToLoft(i_crv._com, i_ori, i_point._com)

    def get_area_law_tolerance_parameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_loft.GetAreaLawToleranceParameter())

    def get_faces_for_closing(self) -> tuple[Reference, Reference]:
        ### assume it this works, need working vba example to confirm
        self.hybrid_shape_loft.GetFacesForClosing()

    def get_guide(self, i_pos: int) -> tuple[Reference, Reference]:
        return self.hybrid_shape_loft.GetGuide(i_pos)

    def get_nb_of_guides(self) -> int:
        return self.hybrid_shape_loft.GetNbOfGuides()

    #def get_section_from_loft(self, i_rank: int, o_crv: Reference, o_ori: int, o_point: Reference) -> tuple:
    #    return self.hybrid_shape_loft.GetSectionFromLoft(i_rank, o_crv.com, o_ori, o_point.com)
    def get_section_from_loft(self, i_rank: int) -> tuple[Reference, int, Reference]:   
        # vba_function_name = 'get_section'
        # vba_code = f"""
        # Public Function {vba_function_name}(obj as HybridShapeLoft, i_pos as Integer) as Variant
        #     Dim oCrv as Reference, oOri as Long, oPoint as Reference
        #     obj.GetSectionFromLoft i_pos, oCrv, oOri, oPoint
        #     {vba_function_name} = Array(oCrv, oOri, oPoint)
        # End Function
        # """
        #return self.application().system_service().evaluate(vba_code, 3, vba_function_name, [self._com, i_rank])
        return self._get_multi(([self._com, i_rank]), ("HybridShapeLoft", "GetSectionFromLoft","Integer"), ("Reference", "Long", "Reference"))

    def get_spine(self) -> tuple:
        return self.hybrid_shape_loft.GetSpine()

    def get_start_and_end_section_tangent(self) -> tuple[Reference, Reference]:
        return self.hybrid_shape_loft.GetStartAndEndSectionTangent()

    def insert_coupling(self, i_position: int) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.InsertCoupling(i_position)
        return self

    def insert_coupling_point(self, i_coupling_index: int, i_position: int, i_point: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.InsertCouplingPoint(i_coupling_index, i_position, i_point._com)
        return self

    def insert_section_to_loft(self, i_type: bool, i_crv: Reference, i_ori: int, i_point: Reference,i_section_ref: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.InsertSectionToLoft(i_type, i_crv._com, i_ori, i_point._com, i_section_ref._com)
        return self

    def modify_guide_curve(self, i_guide: Reference, i_new_guide: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.ModifyGuideCurve(i_guide._com, i_new_guide._com)
        return self

    def modify_section_curve(self, i_section: Reference, i_new_section: Reference) -> tuple: #, o_curve_section: Reference, o_closing_point: Reference, o_pt_diag: int
        ### replace works, but then error is still thrown ###
        #return self.hybrid_shape_loft.ModifySectionCurve(i_section._com, i_new_section._com, o_curve_section._com, o_closing_point._com,o_pt_diag)
        return self._get_multi(([self._com, i_section, i_new_section]),("HybridShapeLoft", "ModifySectionCurve", "Reference", "Reference"),("Reference", "Reference", "Long"))

    def modify_section_orient(self, i_section: Reference, i_orient: int) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.ModifySectionOrient(i_section._com, i_orient)
        return self

    def remove_face_for_closing(self, i_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveFaceForClosing(i_section._com)
        return self

    def remove_guide(self, i_guide: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveGuide(i_guide._com)
        return self

    def remove_guide_tangent(self, i_guide: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveGuideTangent(i_guide._com)
        return self

    def remove_section(self, i_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveSection(i_section._com)
        return self

    def remove_section_point(self, i_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveSectionPoint(i_section._com)
        return self

    def remove_section_tangent(self, i_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.RemoveSectionTangent(i_section._com)
        return self

    def set_end_face_for_closing(self, i_face: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.SetEndFaceForClosing(i_face._com)
        return self

    def set_end_section_tangent(self, i_tangent_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.SetEndSectionTangent(i_tangent_section._com)
        return self

    def set_spine(self, i_spine: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.SetSpine(i_spine._com)
        return self

    def set_start_face_for_closing(self, i_face: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.SetStartFaceForClosing(i_face._com)
        return self

    def set_start_section_tangent(self, i_tangent_section: Reference) -> 'HybridShapeLoft':
        self.hybrid_shape_loft.SetStartSectionTangent(i_tangent_section._com)
        return self

    def __repr__(self):
        return f'HybridShapeLoft(name="{self.name}")'