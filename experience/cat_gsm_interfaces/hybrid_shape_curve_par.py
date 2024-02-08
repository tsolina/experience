from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeCurvePar(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCurvePar
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_curve_par = com

    def curve_offseted(self, value: Reference = None) -> Union['HybridShapeCurvePar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.CurveOffseted = value._com
            return self
        return Reference(self.hybrid_shape_curve_par.CurveOffseted)

    def curve_par_law(self, value: Reference = None) -> Union['HybridShapeCurvePar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.CurveParLaw = value._com
            return self
        return Reference(self.hybrid_shape_curve_par.CurveParLaw)

    def curve_par_type(self, value: int = None) -> Union['HybridShapeCurvePar', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.CurveParType = value
            return self
        return self.hybrid_shape_curve_par.CurveParType

    def geodesic(self, value: bool = None) -> Union['HybridShapeCurvePar', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.Geodesic = value
            return self
        return self.hybrid_shape_curve_par.Geodesic

    def invert_direction(self, value: bool = None) -> Union['HybridShapeCurvePar', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.InvertDirection = value
            return self
        return self.hybrid_shape_curve_par.InvertDirection

    def invert_mapping_law(self, value: bool = None) -> Union['HybridShapeCurvePar', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.InvertMappingLaw = value
            return self
        return self.hybrid_shape_curve_par.InvertMappingLaw

    def keep_both_sides(self, value: bool = None) -> Union['HybridShapeCurvePar', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.KeepBothSides = value
            return self
        return self.hybrid_shape_curve_par.KeepBothSides

    def law_type(self, value: int = None) -> Union['HybridShapeCurvePar', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.LawType = value
            return self
        return self.hybrid_shape_curve_par.LawType

    def maximum_deviation_value(self, value: float = None) -> Union['HybridShapeCurvePar', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.MaximumDeviationValue = value
            return self
        return self.hybrid_shape_curve_par.MaximumDeviationValue

    def offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_curve_par.Offset)

    def offset2(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_curve_par.Offset2)

    def other_side(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.OtherSide)

    def passing_point(self, value: Reference = None) -> Union['HybridShapeCurvePar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.PassingPoint = value._com
            return self
        return Reference(self.hybrid_shape_curve_par.PassingPoint)

    def smoothing_type(self, value: int = None) -> Union['HybridShapeCurvePar', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.SmoothingType = value
            return self
        return self.hybrid_shape_curve_par.SmoothingType

    def support(self, value: Reference = None) -> Union['HybridShapeCurvePar', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.Support = value._com
            return self
        return Reference(self.hybrid_shape_curve_par.Support)

    def p_3d_smoothing(self, value: bool = None) -> Union['HybridShapeCurvePar', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_curve_par.p3DSmoothing = value
            return self
        return self.hybrid_shape_curve_par.p3DSmoothing

    def get_plane_normal(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, 'GetPlaneNormal', 2)

    def put_plane_normal(self, i_normal: tuple) -> 'HybridShapeCurvePar':
        self.hybrid_shape_curve_par.PutPlaneNormal(i_normal)
        return self

    def __repr__(self):
        return f'HybridShapeCurvePar(name="{self.name}")'