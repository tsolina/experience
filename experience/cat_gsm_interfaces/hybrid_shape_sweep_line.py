from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeSweep
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeSweepLine(HybridShapeSweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sweep_line = com

    def angle_law(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.AngleLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.AngleLaw)

    def angle_law_inversion(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.AngleLawInversion = value
            return self
        return self.hybrid_shape_sweep_line.AngleLawInversion

    def angle_law_type(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.AngleLawType = value
            return self
        return self.hybrid_shape_sweep_line.AngleLawType

    def canonical_detection(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.CanonicalDetection = value
            return self
        return self.hybrid_shape_sweep_line.CanonicalDetection

    def context(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.Context = value
            return self
        return self.hybrid_shape_sweep_line.Context

    def draft_computation_mode(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.DraftComputationMode = value
            return self
        return self.hybrid_shape_sweep_line.DraftComputationMode

    def draft_direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeSweepLine', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.DraftDirection = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_sweep_line.DraftDirection)

    def first_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.FirstGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.FirstGuideCrv)

    def first_guide_surf(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.FirstGuideSurf = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.FirstGuideSurf)

    def first_length_law(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.FirstLengthLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.FirstLengthLaw)

    def first_length_law_inversion(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.FirstLengthLawInversion = value
            return self
        return self.hybrid_shape_sweep_line.FirstLengthLawInversion

    def guide_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_sweep_line.GuideDeviation)

    def guide_deviation_activity(self, value: bool = None) -> Union['HybridShapeSweepLine', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.GuideDeviationActivity = value
            return self
        return self.hybrid_shape_sweep_line.GuideDeviationActivity

    def mode(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.Mode = value
            return self
        return self.hybrid_shape_sweep_line.Mode

    def second_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SecondGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.SecondGuideCrv)

    def second_guide_surf(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SecondGuideSurf = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.SecondGuideSurf)

    def second_length_law(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SecondLengthLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.SecondLengthLaw)

    def second_length_law_inversion(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SecondLengthLawInversion = value
            return self
        return self.hybrid_shape_sweep_line.SecondLengthLawInversion

    def second_trim_option(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SecondTrimOption = value
            return self
        return self.hybrid_shape_sweep_line.SecondTrimOption

    def smooth_activity(self, value: bool = None) -> Union['HybridShapeSweepLine', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SmoothActivity = value
            return self
        return self.hybrid_shape_sweep_line.SmoothActivity

    def smooth_angle_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sweep_line.SmoothAngleThreshold)

    def solution_no(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.SolutionNo = value
            return self
        return self.hybrid_shape_sweep_line.SolutionNo

    def spine(self, value: Reference = None) -> Union['HybridShapeSweepLine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.Spine = value._com
            return self
        return Reference(self.hybrid_shape_sweep_line.Spine)

    def trim_option(self, value: int = None) -> Union['HybridShapeSweepLine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_line.TrimOption = value
            return self
        return self.hybrid_shape_sweep_line.TrimOption

    def add_draft_angle_definition_location(self, ip_ia_loc_elem: Reference, i_ang: float) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.AddDraftAngleDefinitionLocation(ip_ia_loc_elem._com, i_ang)
        return self

    def get_angle(self, i_i: int) -> 'Angle':
        return Angle(self.hybrid_shape_sweep_line.GetAngle(i_i))

    def get_angular_law(self) -> tuple['Angle', 'Angle', int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetAngularLaw"), ("Angle", "Angle", "Long"))

    def get_choice_nb_surfaces(self) -> tuple[int, int, int, int, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetChoiceNbSurfaces"), ("Long", "Long", "Long", "Long", "Long"))

    def get_choice_no(self, o_val1: int, o_val2: int, o_val3: int) -> None:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetChoiceNo"), ("Long", "Long", "Long"))

    def get_draft_angle_definition_location(self, i_loc: int, op_ia_element: Reference, o_angle: 'Angle') -> tuple[Reference, "Angle"]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com, i_loc], ("HybridShapeSweepLine","GetDraftAngleDefinitionLocation","Long"), ("Reference", "Angle"))

    def get_draft_angle_definition_locations_nb(self) -> int:
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocationsNb()

    def get_first_length_definition_type(self) -> tuple[int, Reference]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetFirstLengthDefinitionType"), ("Long", "Reference"))

    def get_first_length_law(self) -> tuple["Length", 'Length', int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetFirstLengthLaw"), ("Length", "Length", "Long"))

    def get_length(self, i_i: int) -> 'Length':
        return Length(self.hybrid_shape_sweep_line.GetLength(i_i))

    def get_length_law_types(self) -> tuple[int, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetLengthLawTypes"), ("Long", "Long"))

    def get_longitudinal_relimiters(self) -> tuple[Reference, Reference]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetLongitudinalRelimiters"), ("Reference", "Reference"))

    def get_nb_angle(self) -> int:
        return self.hybrid_shape_sweep_line.GetNbAngle()

    def get_nb_guide_crv(self) -> int:
        return self.hybrid_shape_sweep_line.GetNbGuideCrv()

    def get_nb_guide_sur(self) -> int:
        return self.hybrid_shape_sweep_line.GetNbGuideSur()

    def get_nb_length(self) -> int:
        return self.hybrid_shape_sweep_line.GetNbLength()

    def get_relimiters(self) -> tuple[Reference, int, Reference, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetRelimiters"), ("Reference", "Long", "Reference", "Long"))

    def get_second_length_definition_type(self, o_second_type: int, op_ia_elem: Reference) -> None:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetSecondLengthDefinitionType"), ("Long", "Reference"))

    def get_second_length_law(self) -> tuple["Length", 'Length', int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepLine","GetFirstLengthLaw"), ("Length", "Length", "Long"))
 
    def insert_draft_angle_definition_location(self, i_elem: Reference, i_angle: 'Angle', i_pos: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.InsertDraftAngleDefinitionLocation(i_elem._com, i_angle._com, i_pos)
        return self

    def remove_all_draft_angle_definition_locations(self) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveAllDraftAngleDefinitionLocations()
        return self

    def remove_angle(self) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveAngle()
        return self

    def remove_draft_angle_definition_location_position(self, i_pos: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveDraftAngleDefinitionLocationPosition(i_pos)
        return self

    def remove_guide_crv(self) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveGuideCrv()
        return self

    def remove_guide_sur(self) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveGuideSur()
        return self

    def remove_length(self) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.RemoveLength()
        return self

    def set_angle(self, i_i: int, i_elem: float) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetAngle(i_i, i_elem)
        return self

    def set_angular_law(self, i_start_ang: float, i_end_ang: float, i_law_type: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetAngularLaw(i_start_ang, i_end_ang, i_law_type)
        return self

    def set_choice_nb_surfaces(self, i_surf_ori1: int, i_surf_ori2: int, i_surf_coupl_ori1: int, i_surf_coupl_ori2: int, i_no: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetChoiceNbSurfaces(i_surf_ori1, i_surf_ori2, i_surf_coupl_ori1, i_surf_coupl_ori2, i_no)
        return self

    def set_choice_no(self, i_val1: int, i_val2: int, i_val3: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetChoiceNo(i_val1, i_val2, i_val3)
        return self

    def set_first_length_definition_type(self, i_first_type: int, ip_ia_elem: Reference) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetFirstLengthDefinitionType(i_first_type, ip_ia_elem._com)
        return self

    def set_first_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetFirstLengthLaw(i_length1, i_length2, i_law_type)
        return self

    def set_guide_deviation(self, i_length: float) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetGuideDeviation(i_length)
        return self

    def set_length(self, i_i: int, i_elem: float) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetLength(i_i, i_elem)
        return self

    def set_length_law_types(self, i_first_type: int, i_second_type: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetLengthLawTypes(i_first_type, i_second_type)
        return self

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetLongitudinalRelimiters(ip_ia_elem1._com, ip_ia_elem2._com)
        return self

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetRelimiters(ip_ia_elem1._com, ip_orient1, ip_ia_elem2._com, ip_orient2)
        return self

    def set_second_length_definition_type(self, i_second_type: int, ip_ia_elem: Reference) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetSecondLengthDefinitionType(i_second_type, ip_ia_elem._com)
        return self

    def set_second_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetSecondLengthLaw(i_length1, i_length2, i_law_type)
        return self

    def set_smooth_angle_threshold(self, i_angle: float) -> 'HybridShapeSweepLine':
        self.hybrid_shape_sweep_line.SetSmoothAngleThreshold(i_angle)
        return self

    def __repr__(self):
        return f'HybridShapeSweepLine(name="{self.name}")'