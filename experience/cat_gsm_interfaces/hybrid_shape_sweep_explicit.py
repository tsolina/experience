from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import HybridShapeSweep
from experience.inf_interfaces import Reference

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeSweepExplicit(HybridShapeSweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepExplicit
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sweep_explicit = com

    def angle_law(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.AngleLaw = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.AngleLaw)

    def angle_law_inversion(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.AngleLawInversion = value
            return self
        return self.hybrid_shape_sweep_explicit.AngleLawInversion

    def angle_law_type(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.AngleLawType = value
            return self
        return self.hybrid_shape_sweep_explicit.AngleLawType

    def canonical_detection(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.CanonicalDetection = value
            return self
        return self.hybrid_shape_sweep_explicit.CanonicalDetection

    def context(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.Context = value
            return self
        return self.hybrid_shape_sweep_explicit.Context

    def first_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.FirstGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.FirstGuideCrv)

    def guide_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_sweep_explicit.GuideDeviation)

    def guide_deviation_activity(self, value: bool = None) -> Union['HybridShapeSweepExplicit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.GuideDeviationActivity = value
            return self
        return self.hybrid_shape_sweep_explicit.GuideDeviationActivity

    def guide_projection(self, value: bool = None) -> Union['HybridShapeSweepExplicit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.GuideProjection = value
            return self
        return self.hybrid_shape_sweep_explicit.GuideProjection

    def mode(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.Mode = value
            return self
        return self.hybrid_shape_sweep_explicit.Mode

    def position_mode(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.PositionMode = value
            return self
        return self.hybrid_shape_sweep_explicit.PositionMode

    def positioned_profile(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.PositionedProfile = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.PositionedProfile)

    def profile(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.Profile = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.Profile)

    def profile_x_axis_computation_mode(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode = value
            return self
        return self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode

    def pulling_direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeSweepExplicit', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.PullingDirection = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_sweep_explicit.PullingDirection)

    def reference(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.Profile = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.Reference)

    def second_guide_crv(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.SecondGuideCrv = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.SecondGuideCrv)

    def smooth_activity(self, value: bool = None) -> Union['HybridShapeSweepExplicit', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.SmoothActivity = value
            return self
        return self.hybrid_shape_sweep_explicit.SmoothActivity

    def smooth_angle_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_sweep_explicit.SmoothAngleThreshold)

    def solution_no(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.SolutionNo = value
            return self
        return self.hybrid_shape_sweep_explicit.SolutionNo

    def spine(self, value: Reference = None) -> Union['HybridShapeSweepExplicit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.Spine = value._com
            return self
        return Reference(self.hybrid_shape_sweep_explicit.Spine)

    def sub_type(self, value: int = None) -> Union['HybridShapeSweepExplicit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep_explicit.SubType = value
            return self
        return self.hybrid_shape_sweep_explicit.SubType

    def get_angle_ref(self, ii: int) -> 'Angle':
        return Angle(self.hybrid_shape_sweep_explicit.GetAngleRef(ii))

    def get_fitting_points(self) -> tuple[Reference, Reference]:
        return self.hybrid_shape_sweep_explicit.GetFittingPoints()

    def get_longitudinal_relimiters(self) -> tuple[Reference, Reference]:
        return self.hybrid_shape_sweep_explicit.GetLongitudinalRelimiters()

    def get_nb_angle(self) -> int:
        return self.hybrid_shape_sweep_explicit.GetNbAngle()

    def get_nb_guide(self) -> int:
        return self.hybrid_shape_sweep_explicit.GetNbGuide()

    def get_nb_pos_angle(self) -> int:
        return self.hybrid_shape_sweep_explicit.GetNbPosAngle()

    def get_nb_pos_coord(self) -> int:
        return self.hybrid_shape_sweep_explicit.GetNbPosCoord()

    def get_pos_angle(self, ii: int) -> 'Angle':
        return Angle(self.hybrid_shape_sweep_explicit.GetPosAngle(ii))

    def get_pos_coord(self, ii: int) -> 'Length':
        return Length(self.hybrid_shape_sweep_explicit.GetPosCoord(ii))

    def get_pos_direction(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.GetPosDirection(ii))

    def get_pos_point(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        return self.hybrid_shape_sweep_explicit.GetPosSwapAxes(ii)

    def get_relimiters(self) -> tuple[Reference, int, Reference, int]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeSweepExplicit", "GetRelimiters"), ("Reference", "Long", "Reference", "Long"))

    def is_sketch_axis_used_as_default(self) -> bool:
        return self.hybrid_shape_sweep_explicit.IsSketchAxisUsedAsDefault()

    def remove_angle(self) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.RemoveAngle()
        return self

    def remove_fitting_points(self) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.RemoveFittingPoints()
        return self

    def remove_guide(self) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.RemoveGuide()
        return self

    def set_angle_ref(self, ii: int, elem: float) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetAngleRef(ii, elem)
        return self

    def set_fitting_points(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetFittingPoints(ip_ia_elem_a._com, ip_ia_elem_b._com)
        return self

    def set_guide_deviation(self, i_length: float) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetGuideDeviation(i_length)
        return self

    def set_longitudinal_relimiters(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetLongitudinalRelimiters(ip_ia_elem_a._com, ip_ia_elem_b._com)
        return self

    def set_pos_angle(self, ii: int, elem: float) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetPosAngle(ii, elem)
        return self

    def set_pos_coord(self, ii: int, elem: float) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetPosCoord(ii, elem)
        return self

    def set_pos_direction(self, ii: int, elem: Reference) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetPosDirection(ii, elem._com)
        return self

    def set_pos_point(self, ii: int, elem: Reference) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetPosPoint(ii, elem._com)
        return self

    def set_pos_swap_axes(self, ii: int, elem: int) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetPosSwapAxes(ii, elem)
        return self

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetRelimiters(ip_ia_elem1._com, ip_orient1, ip_ia_elem2._com, ip_orient2)
        return self

    def set_smooth_angle_threshold(self, i_angle: float) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.SetSmoothAngleThreshold(i_angle)
        return self

    def use_sketch_axis_as_default(self, i_boolean: bool) -> 'HybridShapeSweepExplicit':
        self.hybrid_shape_sweep_explicit.UseSketchAxisAsDefault(i_boolean)
        return self

    def __repr__(self):
        return f'HybridShapeSweepExplicit(name="{self.name}")'