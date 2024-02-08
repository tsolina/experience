from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeConic(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeConic
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_conic = com

    def conic_parameter(self, value: float = None) -> Union['HybridShapeConic', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.ConicParameter = value
            return self
        return self.hybrid_shape_conic.ConicParameter

    def conic_user_tol(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_conic.ConicUserTol)

    def end_point(self, value: Reference = None) -> Union['HybridShapeConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.EndPoint = value._com
            return self
        return Reference(self.hybrid_shape_conic.EndPoint)

    def end_tangent(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeConic', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.EndTangent = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_conic.EndTangent)

    def start_point(self, value: Reference = None) -> Union['HybridShapeConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.StartPoint = value._com
            return self
        return Reference(self.hybrid_shape_conic.StartPoint)

    def start_tangent(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeConic', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.StartTangent = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_conic.StartTangent)

    def support_plane(self, value: Reference = None) -> Union['HybridShapeConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.SupportPlane = value._com
            return self
        return Reference(self.hybrid_shape_conic.SupportPlane)

    def tangent_int_point(self, value: Reference = None) -> Union['HybridShapeConic', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_conic.TangentIntPoint = value._com
            return self
        return Reference(self.hybrid_shape_conic.TangentIntPoint)

    def get_end_tangent_direction_flag(self) -> int:
        return self.hybrid_shape_conic.GetEndTangentDirectionFlag()

    def get_intermed_tangent(self, value: int = None) -> 'HybridShapeDirection':
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_conic.GetIntermedTangent(value))

    def get_intermediate_point(self, i_index_point: int) -> Reference:
        return self.hybrid_shape_conic.GetIntermediatePoint(i_index_point)

    def get_intermediate_tangent_direction_flag(self, i_index_point: int) -> int:
        return self.hybrid_shape_conic.GetIntermediateTangentDirectionFlag(i_index_point)

    def get_start_tangent_direction_flag(self) -> int:
        return self.hybrid_shape_conic.GetStartTangentDirectionFlag()

    def set_end_tangent_direction_flag(self, i_orientation: int) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetEndTangentDirectionFlag(i_orientation)
        return self

    def set_intermediate_point(self, i_index_point: int, i_end_point: Reference) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetIntermediatePoint(i_index_point, i_end_point._com)
        return self

    def set_intermediate_tangent(self, i_index_point: int, i_tgt_dir: 'HybridShapeDirection') -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetIntermediateTangent(i_index_point, i_tgt_dir._com)
        return self

    def set_intermediate_tangent_direction_flag(self, i_index_point: int, i_orientation: int) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetIntermediateTangentDirectionFlag(i_index_point, i_orientation)
        return self

    def set_start_and_end_tangents_plus_conic_parameter(self, i_start_tgt: 'HybridShapeDirection', i_end_tgt: 'HybridShapeDirection', i_conic_param: float) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetStartAndEndTangentsPlusConicParameter(i_start_tgt._com,i_end_tgt._com, i_conic_param)
        return self

    def set_start_and_end_tangents_plus_passing_point(self, i_start_tgt: 'HybridShapeDirection', i_end_tgt: 'HybridShapeDirection', i_passing_pt: Reference) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetStartAndEndTangentsPlusPassingPoint(i_start_tgt._com, i_end_tgt._com, i_passing_pt._com)
        return self

    def set_start_tangent_direction_flag(self, i_orientation: int) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetStartTangentDirectionFlag(i_orientation)
        return self

    def set_tangent_intersect_point_plus_conic_parm(self, i_tgt_int: Reference, i_conic_param: float) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetTangentIntersectPointPlusConicParm(i_tgt_int._com, i_conic_param)
        return self

    def set_tangent_intersect_point_plus_passing_point(self, i_tgt_int: Reference, i_passing_pt: Reference) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetTangentIntersectPointPlusPassingPoint(i_tgt_int._com, i_passing_pt._com)
        return self

    def set_three_intermediate_passing_points(self, i_pass_pt1: Reference, i_pass_pt2: Reference, i_pass_pt3: Reference) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetThreeIntermediatePassingPoints(i_pass_pt1._com, i_pass_pt2._com, i_pass_pt3._com)
        return self

    def set_two_intermediate_passing_points_plus_one_tangent(self, i_pass_pt1: Reference, i_pass_pt2: Reference, i_tgt_dir: 'HybridShapeDirection', i_index_point: int) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SetTwoIntermediatePassingPointsPlusOneTangent(i_pass_pt1._com, i_pass_pt2._com, i_tgt_dir._com, i_index_point)
        return self

    def switch_end_tangent_direction(self) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SwitchEndTangentDirection()
        return self

    def switch_intermediate_tangent_direction(self, i_index_point: int) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SwitchIntermediateTangentDirection(i_index_point)
        return self

    def switch_start_tangent_direction(self) -> 'HybridShapeConic':
        self.hybrid_shape_conic.SwitchStartTangentDirection()
        return self

    def __repr__(self):
        return f'HybridShapeConic(name="{self.name}")'