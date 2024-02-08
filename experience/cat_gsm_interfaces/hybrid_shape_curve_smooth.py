from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference

from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeCurveSmooth(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCurveSmooth
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_curve_smooth = com

    def correction_mode(self, value: int = None) -> Union['HybridShapeCurveSmooth', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.CorrectionMode = value
            return self
        return self.hybrid_shape_curve_smooth.CorrectionMode

    def curvature_threshold(self, value: float = None) -> Union['HybridShapeCurveSmooth', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.CurvatureThreshold = value
            return self
        return self.hybrid_shape_curve_smooth.CurvatureThreshold

    def curvature_threshold_activity(self, value: bool = None) -> Union['HybridShapeCurveSmooth', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.CurvatureThresholdActivity = value
            return self
        return self.hybrid_shape_curve_smooth.CurvatureThresholdActivity

    def curve_to_smooth(self, value: Reference = None) -> Union['HybridShapeCurveSmooth', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.CurveToSmooth = value._com
            return self
        return Reference(self.hybrid_shape_curve_smooth.CurveToSmooth)

    def end_extremity_continuity(self, value: int = None) -> Union['HybridShapeCurveSmooth', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.EndExtremityContinuity = value
            return self
        return self.hybrid_shape_curve_smooth.EndExtremityContinuity

    def maximum_deviation(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_curve_smooth.MaximumDeviation)

    def maximum_deviation_activity(self, value: bool = None) -> Union['HybridShapeCurveSmooth', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.MaximumDeviationActivity = value
            return self
        return self.hybrid_shape_curve_smooth.MaximumDeviationActivity

    def start_extremity_continuity(self, value: int = None) -> Union['HybridShapeCurveSmooth', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.StartExtremityContinuity = value
            return self
        return self.hybrid_shape_curve_smooth.StartExtremityContinuity

    def support(self, value: Reference = None) -> Union['HybridShapeCurveSmooth', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.Support = value._com
            return self
        return Reference(self.hybrid_shape_curve_smooth.Support)

    def tangency_threshold(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_curve_smooth.TangencyThreshold)

    def topology_simplification_activity(self, value: bool = None) -> Union['HybridShapeCurveSmooth', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_smooth.TopologySimplificationActivity = value
            return self
        return self.hybrid_shape_curve_smooth.TopologySimplificationActivity

    def add_frozen_curve_segment(self, i_curve: Reference) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.AddFrozenCurveSegment(i_curve._com)
        return self

    def add_frozen_point(self, i_point: Reference) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.AddFrozenPoint(i_point._com)
        return self

    def get_frozen_curve_segment(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenCurveSegment(i_pos))

    def get_frozen_curve_segments_size(self) -> int:
        return self.hybrid_shape_curve_smooth.GetFrozenCurveSegmentsSize()

    def get_frozen_point(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenPoint(i_pos))

    def get_frozen_points_size(self) -> int:
        return self.hybrid_shape_curve_smooth.GetFrozenPointsSize()

    def remove_all_frozen_curve_segments(self) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.RemoveAllFrozenCurveSegments()
        return self

    def remove_all_frozen_points(self) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.RemoveAllFrozenPoints()
        return self

    def remove_frozen_curve_segment(self, i_curve: Reference) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.RemoveFrozenCurveSegment(i_curve._com)
        return self

    def remove_frozen_point(self, i_point: Reference) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.RemoveFrozenPoint(i_point.com)
        return self

    def set_maximum_deviation(self, i_max_deviation: float) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.SetMaximumDeviation(i_max_deviation)
        return self

    def set_tangency_threshold(self, i_tangency_threshold: float) -> 'HybridShapeCurveSmooth':
        self.hybrid_shape_curve_smooth.SetTangencyThreshold(i_tangency_threshold)
        return self

    def __repr__(self):
        return f'HybridShapeCurveSmooth(name="{self.name}")'