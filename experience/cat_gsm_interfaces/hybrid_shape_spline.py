from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length, RealParam

class HybridShapeSpline(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSpline
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_spline = com

    def add_point(self, ip_ia_point: Reference) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.AddPoint(ip_ia_point._com)
        return self

    def add_point_with_constraint_explicit(
            self,
            ip_ia_point: Reference,
            ip_ia_dir_tangency: 'HybridShapeDirection',
            i_tangency_norm: float,
            i_inverse_tangency: int,
            ip_ia_dir_curvature: 'HybridShapeDirection',
            i_curvature_radius: float) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.AddPointWithConstraintExplicit(ip_ia_point._com,
                                                                       ip_ia_dir_tangency._com,
                                                                       i_tangency_norm,
                                                                       i_inverse_tangency,
                                                                       ip_ia_dir_curvature._com,
                                                                       i_curvature_radius)
        return self

    def add_point_with_constraint_from_curve(self, ip_ia_point: Reference, ip_ia_curve_cst: Reference,
                                             i_tangency_norm: float, i_invert_value: int, i_crv_cst_type: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.AddPointWithConstraintFromCurve(ip_ia_point._com,
                                                                        ip_ia_curve_cst._com, i_tangency_norm,
                                                                        i_invert_value, i_crv_cst_type)
        return self

    def get_closure(self) -> int:
        return self.hybrid_shape_spline.GetClosure()

    def get_constraint_type(self, i_pos: int) -> int:
        return self.hybrid_shape_spline.GetConstraintType(i_pos)

    def get_curvature_radius(self, i_pos: int) -> 'Length':
        return Length(self.hybrid_shape_spline.GetCurvatureRadius(i_pos))

    def get_direction_inversion(self, i_pos: int) -> int:
        return self.hybrid_shape_spline.GetDirectionInversion(i_pos)

    def get_nb_control_point(self) -> int:
        return self.hybrid_shape_spline.GetNbControlPoint()

    def get_point(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_spline.GetPoint(i_pos))

    def get_point_constraint_explicit(self, i_pos: int) -> tuple:
        return self._get_multi([self._com, i_pos], ("HybridShapeSpline", "GetPointConstraintExplicit", "Long"), ("HybridShapeDirection", "Double", "Long", "HybridShapeDirection", "Double"))

    def get_point_constraint_from_curve(self, i_pos: int) -> tuple:
        return self._get_multi([self._com, i_pos], ("HybridShapeSpline", "GetPointConstraintExplicit", "Long"),("Reference", "Double", "Long", "Long"))

    def get_point_position(self, ip_ia_point: Reference) -> int:
        return self.hybrid_shape_spline.GetPointPosition(ip_ia_point.com)

    def get_spline_type(self) -> int:
        return self.hybrid_shape_spline.GetSplineType()

    def get_support(self) -> Reference:
        return Reference(self.hybrid_shape_spline.GetSupport())

    def get_tangent_norm(self, i_pos: int) -> 'RealParam':
        return RealParam(self.hybrid_shape_spline.GetTangentNorm(i_pos))

    def invert_direction(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.InvertDirection(i_pos)
        return self

    def remove_all(self) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveAll()
        return self

    def remove_control_point(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveControlPoint(i_pos)
        return self

    def remove_curvature_radius_direction(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveCurvatureRadiusDirection(i_pos)
        return self

    def remove_curvature_radius_value(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveCurvatureRadiusValue(i_pos)
        return self

    def remove_support(self) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveSupport()
        return self

    def remove_tangent_direction(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveTangentDirection(i_pos)
        return self

    def remove_tension(self, i_pos: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.RemoveTension(i_pos)
        return self

    def replace_point_at_position(self, i_pos: int, i_point: Reference) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.ReplacePointAtPosition(i_pos, i_point._com)
        return self

    def set_closing(self, i_closing_type: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetClosing(i_closing_type)
        return self

    def set_point_after(self, i_pos: int, ip_ia_point: Reference) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetPointAfter(i_pos, ip_ia_point._com)
        return self

    def set_point_before(self, i_pos: int, ip_ia_point: Reference) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetPointBefore(i_pos, ip_ia_point._com)
        return self

    def set_point_constraint_explicit(self, i_pos: int, ip_ia_dir_tangency: 'HybridShapeDirection',
                                      i_tangency_norm: float, i_inverse_tangency: int,
                                      ip_ia_dir_curvature: 'HybridShapeDirection', i_curvature_radius: float) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetPointConstraintExplicit(i_pos, ip_ia_dir_tangency._com,
                                                                   i_tangency_norm, i_inverse_tangency,
                                                                   ip_ia_dir_curvature._com, i_curvature_radius)
        return self

    def set_point_constraint_from_curve(self, i_pos: int, ip_ia_curve_cst: Reference, i_tangency_norm: float,
                                        i_invert_value: int, i_crv_cst_type: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetPointConstraintFromCurve(i_pos, ip_ia_curve_cst._com, i_tangency_norm,
                                                                    i_invert_value, i_crv_cst_type)
        return self

    def set_spline_type(self, i_spline_type: int) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetSplineType(i_spline_type)
        return self

    def set_support(self, i_support: Reference) -> 'HybridShapeSpline':
        self.hybrid_shape_spline.SetSupport(i_support._com)
        return self

    def __repr__(self):
        return f'HybridShapeSpline(name="{self.name}")'