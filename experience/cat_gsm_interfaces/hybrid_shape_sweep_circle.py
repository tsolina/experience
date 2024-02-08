from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeSweep
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeSweepCircle(HybridShapeSweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepCircle
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sweep_circle = com

    def canonical_detection(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.CanonicalDetection = value
            return self
        return self.hybrid_shape_sweep_circle.CanonicalDetection

    def choice_no(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.ChoiceNo = value
            return self
        return self.hybrid_shape_sweep_circle.ChoiceNo

    def context(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.Context = value
            return self
        return self.hybrid_shape_sweep_circle.Context

    def first_angle_law(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.FirstAngleLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.FirstAngleLaw)

    def first_angle_law_inversion(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.FirstAngleLawInversion = value
            return self
        return self.hybrid_shape_sweep_circle.FirstAngleLawInversion

    def first_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.FirstGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.FirstGuideCrv)

    def guide_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_sweep_circle.GuideDeviation)

    def guide_deviation_activity(self, value: bool = None) -> Union['HybridShapeSweepCircle', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.GuideDeviationActivity = value
            return self
        return self.hybrid_shape_sweep_circle.GuideDeviationActivity

    def mode(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.Mode = value
            return self
        return self.hybrid_shape_sweep_circle.Mode

    def radius_law(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.RadiusLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.RadiusLaw)

    def radius_law_inversion(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.RadiusLawInversion = value
            return self
        return self.hybrid_shape_sweep_circle.RadiusLawInversion

    def radius_law_type(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.RadiusLawType = value
            return self
        return self.hybrid_shape_sweep_circle.RadiusLawType

    def reference(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.Reference = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.Reference)

    def second_angle_law(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.SecondAngleLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.SecondAngleLaw)

    def second_angle_law_inversion(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.SecondAngleLawInversion = value
            return self
        return self.hybrid_shape_sweep_circle.SecondAngleLawInversion

    def second_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.SecondGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.SecondGuideCrv)

    def smooth_activity(self, value: bool = None) -> Union['HybridShapeSweepCircle', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.SmoothActivity = value
            return self
        return self.hybrid_shape_sweep_circle.SmoothActivity

    def smooth_angle_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sweep_circle.SmoothAngleThreshold)

    def spine(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.Spine = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.Spine)

    def third_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepCircle', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.ThirdGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_circle.ThirdGuideCrv)

    def trim_option(self, value: int = None) -> Union['HybridShapeSweepCircle', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_circle.TrimOption = value
            return self
        return self.hybrid_shape_sweep_circle.TrimOption

    def get_angle(self, i_i: int) -> 'Angle':
        return Angle(self.hybrid_shape_sweep_circle.GetAngle(i_i))

    def get_angle_law_types(self) -> tuple[int, int]:
        return self.hybrid_shape_sweep_circle.GetAngleLawTypes()

    def get_first_angle_law(self) -> tuple["Angle", "Angle", int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepCircle","GetRelimiters"), ("Angle", "Angle", "Long"))

    def get_longitudinal_relimiters(self) -> tuple[Reference, Reference]:
        return self.hybrid_shape_sweep_circle.GetLongitudinalRelimiters()

    def get_nb_angle(self) -> int:
        return self.hybrid_shape_sweep_circle.GetNbAngle()

    def get_nb_guide(self) -> int:
        return self.hybrid_shape_sweep_circle.GetNbGuide()

    def get_nb_radius(self) -> int:
        return self.hybrid_shape_sweep_circle.GetNbRadius()

    def get_radius(self, i_i: int) -> 'Length':
        return Length(self.hybrid_shape_sweep_circle.GetRadius(i_i))

    def get_relimiters(self) -> tuple[Reference, int, Reference, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepCircle","GetRelimiters"), ("Reference", "Long", "Reference", "Long"))

    def get_second_angle_law(self) -> tuple:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepCircle","GetSecondAngleLaw"), ("Angle", "Angle", "Long"))

    def get_tangency_choice_no(self) -> tuple:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepCircle", "GetTangencyChoiceNo"), ("Long", "Long", "Long"))

    def remove_angle(self) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.RemoveAngle()
        return self

    def remove_guide(self) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.RemoveGuide()
        return self

    def remove_radius(self) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.RemoveRadius()
        return self

    def set_angle(self, i_i: int, i_elem: float) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetAngle(i_i, i_elem)
        return self

    def set_angle_law_types(self, i_first_type: int, i_second_type: int) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetAngleLawTypes(i_first_type, i_second_type)
        return self

    def set_first_angle_law(self, i_elem1: float, i_elem2: float, il_law_type: int) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetFirstAngleLaw(i_elem1, i_elem2, il_law_type)
        return self

    def set_guide_deviation(self, i_length: float) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetGuideDeviation(i_length)
        return self

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetLongitudinalRelimiters(ip_ia_elem1._com, ip_ia_elem2._com)
        return self

    def set_radius(self, i_i: int, i_radius: float) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetRadius(i_i, i_radius)
        return self

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetRelimiters(ip_ia_elem1._com, ip_orient1, ip_ia_elem2._com, ip_orient2)
        return self

    def set_second_angle_law(self, i_elem1: float, i_elem2: float, il_law_type: int) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetSecondAngleLaw(i_elem1, i_elem2, il_law_type)
        return self

    def set_smooth_angle_threshold(self, i_angle: float) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetSmoothAngleThreshold(i_angle)
        return self

    def set_tangency_choice_no(self, i_shell_ori: int, i_guide_ori: int, i_no: int) -> 'HybridShapeSweepCircle':
        self.hybrid_shape_sweep_circle.SetTangencyChoiceNo(i_shell_ori, i_guide_ori, i_no)
        return self

    def __repr__(self):
        return f'HybridShapeSweepCircle(name="{self.name}")'