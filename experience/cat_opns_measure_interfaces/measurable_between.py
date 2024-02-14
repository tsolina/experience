from typing import TYPE_CHECKING
from experience.cat_opns_measure_interfaces import MeasurableInContext

if TYPE_CHECKING:
    from experience.system import AnyObject

class MeasurableBetween(MeasurableInContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         MeasurableBetween
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_between = com

    def angle_to(self, i_other_object: 'AnyObject', i_other_math_axis: tuple = None) -> tuple[float, float, float, float, float, float, float]:
        i_other_math_axis =  i_other_math_axis if i_other_math_axis is not None else [None] * 12
        return self._get_multi([self.measurable_between, i_other_object._com, i_other_math_axis],
                               ("MeasurableBetween", "AngleTo", "AnyObject", "Variant"),
                               ("Double", "Double", "Double", "Double", "Double", "Double", "Double"))

    def angle_to_value_only(self, i_other_object: 'AnyObject', i_other_math_axis: tuple = None) -> float:
        return self.angle_to(i_other_object, i_other_math_axis)[0]

    def distance_min_to(self, i_other_object: 'AnyObject', i_other_math_axis: tuple = None) -> tuple[float, float, float, float, float, float, float]:
        i_other_math_axis =  i_other_math_axis if i_other_math_axis is not None else [None] * 12
        return self._get_multi([self.measurable_between, i_other_object._com, i_other_math_axis],
                               ("MeasurableBetween", "DistanceMinTo", "AnyObject", "Variant"),
                               ("Double", "Double", "Double", "Double", "Double", "Double", "Double"))
    
    def distance_min_to_value_only(self, i_other_object: 'AnyObject', i_other_math_axis: tuple = None) -> float:
        return self.distance_min_to(i_other_object, i_other_math_axis)[0]


    def distance_min_to_as(self, i_other_object: 'AnyObject', i_other_math_axis: tuple) -> tuple[float, float, float, float, float, float, float]:
        i_other_math_axis =  i_other_math_axis if i_other_math_axis is not None else [None] * 12
        return self._get_multi([self.measurable_between, i_other_object._com, i_other_math_axis],
                               ("MeasurableBetween", "DistanceMinToAS", "AnyObject", "Variant"),
                               ("Double", "Double", "Double", "Double", "Double", "Double", "Double"))

    def distance_min_to_point(self, ix_point: float, iy_point: float, iz_point: float) -> tuple[float, float, float, float]:
        return self._get_multi([self.measurable_between, ix_point, iy_point, iz_point],
                               ("MeasurableBetween", "DistanceMinToPoint", "Double", "Double", "Double"),
                               ("Double", "Double", "Double", "Double"))

    def set_computation_mode(self, i_computation_mode: int) -> 'MeasurableBetween':
        """
        enum CATMeasurableModeOfCalc {
        MeasExactCalculation,
        MeasApproximateCalculation,
        MeasExactElseApproxCalculation,
        MeasUnknownCalculation
        }
        """
        self.measurable_between.SetComputationMode(i_computation_mode)
        return self

    def __repr__(self):
        return f'MeasurableBetween(name="{self.name()}")'
