from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length, RealParam

class HybridShapeBlend(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeBlend
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_blend = com

    def coupling(self, value: int = None) -> Union['HybridShapeBlend', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_blend.Coupling = value
            return self
        return self.hybrid_shape_blend.Coupling
    
    def get_coupling(self) -> int:
        return self.hybrid_shape_blend.Coupling

    def set_coupling(self, value: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.Coupling = value
        return self

    def ruled_developable_surface(self, value: bool = None) -> Union['HybridShapeBlend', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_blend.RuledDevelopableSurface = value
            return self
        return self.hybrid_shape_blend.RuledDevelopableSurface

    def smooth_angle_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_blend.SmoothAngleThreshold)

    def smooth_angle_threshold_activity(self, value: bool = None) -> Union['HybridShapeBlend', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_blend.SmoothAngleThresholdActivity = value
            return self
        return self.hybrid_shape_blend.SmoothAngleThresholdActivity

    def smooth_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_blend.SmoothDeviation)

    def smooth_deviation_activity(self, value: bool = None) -> Union['HybridShapeBlend', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_blend.SmoothDeviationActivity = value
            return self
        return self.hybrid_shape_blend.SmoothDeviationActivity

    def spine(self, value: Reference = None) -> Union['HybridShapeBlend', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_blend.SmoothDeviationActivity = value._com
            return self
        return Reference(self.hybrid_shape_blend.Spine)

    def get_border_mode(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetBorderMode(i_blend_limit)

    def get_closing_point(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetClosingPoint(i_blend_limit))

    def get_continuity(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetContinuity(i_blend_limit)

    def get_curve(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetCurve(i_blend_limit))

    def get_orientation(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetOrientation(i_blend_limit)

    def get_ruled_developable_surface_connection(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetRuledDevelopableSurfaceConnection(i_blend_limit)

    def get_support(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetSupport(i_blend_limit))

    def get_tension_in_double(self, i_blend_limit: int, i_rank: int) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_blend.GetTensionInDouble(i_blend_limit, i_rank))

    def get_tension_type(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTensionType(i_blend_limit)

    def get_transition(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTransition(i_blend_limit)

    def get_trim_support(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTrimSupport(i_blend_limit)

    def insert_coupling(self, i_position: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.InsertCoupling(i_position)
        return self

    def insert_coupling_point(self, i_coupling_index: int, i_position: int, i_point: Reference) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.InsertCouplingPoint(i_coupling_index, i_position, i_point._com)
        return self

    def set_border_mode(self, i_blend_limit: int, i_border: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetBorderMode(i_blend_limit, i_border)
        return self
    
    def border_mode(self, i_blend_limit: int, i_border: int = None) -> Union['HybridShapeBlend', int]:
        """ set value if provided and return self, otherwise reads the value """
        if i_border is not None:
            self.hybrid_shape_blend.SetBorderMode(i_blend_limit, i_border)
            return self
        return self.hybrid_shape_blend.GetBorderMode(i_blend_limit)

    def set_closing_point(self, i_blend_limit: int, i_closing_point: Reference) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetClosingPoint(i_blend_limit, i_closing_point._com)
        return self

    def set_continuity(self, i_blend_limit: int, i_continuity: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetContinuity(i_blend_limit, i_continuity)
        return self

    def set_curve(self, i_blend_limit: int, i_curve: Reference) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetCurve(i_blend_limit, i_curve.com)
        return self

    def set_orientation(self, i_blend_limit: int, i_orientation: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetOrientation(i_blend_limit, i_orientation)
        return self

    def set_ruled_developable_surface_connection(self, i_blend_limit: int, i_blend_connection: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetRuledDevelopableSurfaceConnection(i_blend_limit, i_blend_connection)
        return self

    def set_smooth_angle_threshold(self, i_angle: float) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetSmoothAngleThreshold(i_angle)
        return self

    def set_smooth_deviation(self, i_length: float) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetSmoothDeviation(i_length)
        return self

    def set_support(self, i_blend_limit: int, i_support: Reference) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetSupport(i_blend_limit, i_support._com)
        return self

    def set_tension_in_double(self, i_blend_limit: int, i_tension_type: int, i_first_tension: float, i_second_tension: float) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetTensionInDouble(i_blend_limit, i_tension_type, i_first_tension, i_second_tension)
        return self

    def set_tension_type(self, i_blend_limit: int, i_tension_type: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetTensionType(i_blend_limit, i_tension_type)
        return self

    def set_transition(self, i_blend_limit: int, i_transition: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetTransition(i_blend_limit, i_transition)
        return self

    def set_trim_support(self, i_blend_limit: int, i_trim_support: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.SetTrimSupport(i_blend_limit, i_trim_support)
        return self

    def unset_closing_point(self, i_blend_limit: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.UnsetClosingPoint(i_blend_limit)
        return self

    def unset_support(self, i_blend_limit: int) -> 'HybridShapeBlend':
        self.hybrid_shape_blend.UnsetSupport(i_blend_limit)
        return self

    def __repr__(self):
        return f'HybridShapeBlend(name="{self.name}")'