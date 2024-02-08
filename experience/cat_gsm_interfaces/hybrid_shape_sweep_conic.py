from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeSweep
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeSweepConic(HybridShapeSweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepConic
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sweep_conic = com

    def canonical_detection(self, value: int = None) -> Union['HybridShapeSweepConic', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.CanonicalDetection = value
            return self
        return self.hybrid_shape_sweep_conic.CanonicalDetection

    def fifth_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.FifthGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.FifthGuideCrv)

    def first_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.FirstGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.FirstGuideCrv)

    def fourth_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.FourthGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.FourthGuideCrv)

    def guide_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_sweep_conic.GuideDeviation)

    def guide_deviation_activity(self, value: bool = None) -> Union['HybridShapeSweepConic', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.GuideDeviationActivity = value
            return self
        return self.hybrid_shape_sweep_conic.GuideDeviationActivity

    def parameter(self, value: float = None) -> Union['HybridShapeSweepConic', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.GuideDeviationActivity = value
            return self
        return self.hybrid_shape_sweep_conic.Parameter

    def parameter_law(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.ParameterLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.ParameterLaw)

    def parameter_law_inversion(self, value: bool = None) -> Union['HybridShapeSweepConic', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.ParameterLawInversion = value
            return self
        return self.hybrid_shape_sweep_conic.ParameterLawInversion

    def parameter_law_type(self, value: int = None) -> Union['HybridShapeSweepConic', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.ParameterLawType = value
            return self
        return self.hybrid_shape_sweep_conic.ParameterLawType

    def second_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.SecondGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.SecondGuideCrv)

    def smooth_activity(self, value: bool = None) -> Union['HybridShapeSweepConic', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.SmoothActivity = value
            return self
        return self.hybrid_shape_sweep_conic.SmoothActivity

    def smooth_angle_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sweep_conic.SmoothAngleThreshold)

    def spine(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.Spine = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.Spine)

    def third_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_conic.ThirdGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_conic.ThirdGuideCrv)

    def get_longitudinal_relimiters(self) -> tuple[Reference, Reference]:
        return self.hybrid_shape_sweep_conic.GetLongitudinalRelimiters()

    def get_nb_guides(self) -> int:
        return self.hybrid_shape_sweep_conic.GetNbGuides()

    def get_parameter_law(self) -> tuple[float, float, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepConic","GetParameterLaw"), ("Double", "Double", "Long"))

    def get_relimiters(self, op_ia_elem1: Reference, op_orient1: int, op_ia_elem2: Reference, op_orient2: int) -> tuple[Reference, int, Reference, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepConic","GetRelimiters"), ("Reference", "Long", "Reference", "Long"))

    def get_tangency(self, i_index: int) -> tuple[Reference, 'Angle', 'Angle', int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com, i_index], ("HybridShapeSweepConic", "GetTangency", "Long"), ("Reference", "Angle", "Angle", "Long"))

    def get_tangency_angle_law_inversion(self, i_index: int) -> int:
        return self.hybrid_shape_sweep_conic.GetTangencyAngleLawInversion(i_index)

    def get_tangency_law(self, i_index: int) -> tuple[Reference, Reference]:
        return self.hybrid_shape_sweep_conic.GetTangencyLaw(i_index)

    def remove_guide(self, i_index: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.RemoveGuide(i_index)
        return self

    def remove_parameter(self) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.RemoveParameter()
        return self

    def remove_tangency(self, i_index: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.RemoveTangency(i_index)
        return self

    def set_guide_deviation(self, i_length: float) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetGuideDeviation(i_length)
        return self

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetLongitudinalRelimiters(ip_ia_elem1._com, ip_ia_elem2._com)
        return self

    def set_parameter_law(self, i_param_start: float, i_param_end: float, i_law_type: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetParameterLaw(i_param_start, i_param_end, i_law_type)
        return self

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetRelimiters(ip_ia_elem1._com, ip_orient1, ip_ia_elem2._com, ip_orient2)
        return self

    def set_smooth_angle_threshold(self, i_angle: float) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetSmoothAngleThreshold(i_angle)
        return self

    def set_tangency(self, ip_ia_elem: Reference, i_angle_start: float, i_angle_end: float, ilaw_type: int, i_index: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetTangency(ip_ia_elem._com, i_angle_start, i_angle_end, ilaw_type, i_index)
        return self

    def set_tangency_angle_law_inversion(self, i_index: int, i_inversion: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetTangencyAngleLawInversion(i_index, i_inversion)
        return self

    def set_tangency_law(self, ip_ia_elem: Reference, ip_ia_law: Reference, i_index: int) -> 'HybridShapeSweepConic':
        self.hybrid_shape_sweep_conic.SetTangencyLaw(ip_ia_elem._com, ip_ia_law._com, i_index)
        return self

    def __repr__(self):
        return f'HybridShapeSweepConic(name="{self.name}")'