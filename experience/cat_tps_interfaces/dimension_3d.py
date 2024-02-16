from pycatia.drafting_interfaces.drawing_dimension import DrawingDimension
from experience.system import AnyObject
from experience.cat_tps_interfaces import ControledRadius, DimensionLimit, DimensionPattern, EnvelopCondition

class Dimension3D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Dimension3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.dimension_3d = com


    def controled_radius(self) -> ControledRadius:
        return ControledRadius(self.dimension_3d.ControledRadius())


    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.dimension_3d.DimensionLimit())


    def dimension_pattern(self) -> DimensionPattern:
        return DimensionPattern(self.dimension_3d.DimensionPattern())


    def envelope_condition(self) -> EnvelopCondition:
        return EnvelopCondition(self.dimension_3d.EnvelopCondition())


    def get_2d_annot(self) -> DrawingDimension:
        return DrawingDimension(self.dimension_3d.Get2dAnnot())

    def has_a_controlled_radius(self) -> bool:
        return self.dimension_3d.HasAControledRadius()

    def has_an_envelope_condition(self) -> bool:
        return self.dimension_3d.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        return self.dimension_3d.HasDimensionLimit()

    def is_a_continous_feature_applied(self) -> bool:
        return self.dimension_3d.IsAContinuousFeatureApplied()

    def is_a_dimension_pattern(self) -> bool:
        return self.dimension_3d.IsADimensionPattern()

    def move_value(self, x: float, y: float, sub_part: int, dim_angle_behavior: int) -> 'Dimension3D':
        self.dimension_3d.MoveValue(x, y, sub_part, dim_angle_behavior)
        return self

    def __repr__(self):
        return f'Dimension3D(name="{self.name()}")'
