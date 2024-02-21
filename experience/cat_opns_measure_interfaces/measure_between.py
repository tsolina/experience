from experience.system import AnyObject
from experience.cat_opns_measure_interfaces.opns_measure_types import *

class MeasureBetween(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MeasureBetween
    """

    def __init__(self, com):
        super().__init__(com)
        self.measure_between = com

    def compute(self) -> 'MeasureBetween':
        return self.measure_between.Compute()
    
    def get_angle(self) -> 'MeasureBetween':
        return self.measure_between.GetAngle()
    
    def get_axis_system_from_measurable(self) -> tuple:
        return self._get_multi(self.measure_between, "GetAxisSystemFromMeasure", 11)

    def get_band_analysis_parameters(self) -> tuple[float, float, float]:
        return self.measure_between.GetBandAnalysisParameters()
    
    def get_components(self) -> tuple:
        return self._get_multi(self.measure_between, "GetComponents", "") # - to test -
    
    def get_computation_mode(self) -> CATMeasurableModeOfCalc:
        return CATMeasurableModeOfCalc.item(self.measure_between.GetComputationMode())

    def get_distance(self) -> float:
        return self.measure_between.GetDistance()
    
    def get_distance_measure_type(self) -> CATOpnsMeasureDistanceType:
        return CATOpnsMeasureDistanceType.item(self.measure_between.GetDistanceMeasureType())

    def get_distance_measure_type(self) -> CATOpnsMeasureExtensionMode:
        return CATOpnsMeasureExtensionMode.item(self.measure_between.GetDistanceMeasureType())
    # to test
    def get_extension_mode(self) -> tuple[int, CATOpnsMeasureExtensionMode, CATOpnsMeasureExtensionMode]:
        rVal = self.measure_between.GetExtensionMode()
        return (rVal[0], CATOpnsMeasureExtensionMode.item(rVal[1]), CATOpnsMeasureExtensionMode.item(rVal[2]))
    
    def get_first_point_coordinates(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.measure_between, "GetFirstPointCoordinates", 2)

    def get_first_selection(self) -> tuple:
        return self._get_multi(self.measure_between, "GetFirstSelection", "") # - to test -

    def get_result_computation_type(self) -> CATResultCalcType:
        return CATResultCalcType.item(self.measure_between.GetResultComputationType())

    def get_second_point_coordinates(self) -> tuple[float, float, float]:
        return self._get_safe_array(self.measure_between, "GetSecondPointCoordinates", 2)

    def get_second_selection(self) -> tuple:
        return self._get_multi(self.measure_between, "GetSecondSelection", "") # - to test -
    # to test
    def get_selection_calculation_types(self) -> tuple[CATResultCalcType, CATResultCalcType]:
        r_val = self.measure_between.GetSelectionCalculationTypes()
        return tuple(CATResultCalcType.item(r_val[0]), CATResultCalcType.item(r_val[1]))
    
    def set_along_direction(self, ix_vector: float, iy_vector: float, iz_vector: float) -> 'MeasureBetween':
        self.measure_between.SetAlongDirection(ix_vector, iy_vector, iz_vector)
        return self

    def set_axis_system_on_measure(self, i_axis_positioning: list) -> 'MeasureBetween':
        self.measure_between.SetAxisSystemOnMeasure(i_axis_positioning)
        return self
    
    def set_band_analysis_parameters(self, i_min_distance: float, i_max_distance: float, i_accuracy: float) -> 'MeasureBetween':
        self.measure_between.SetBandAnalysisParameters(i_min_distance, i_max_distance, i_accuracy)
        return self
    
    def set_computation_mode(self, i_computation_mode: CATMeasurableModeOfCalc) -> 'MeasureBetween':
        self.measure_between.SetComputationMode(int(i_computation_mode))
        return self
    
    def set_distance_measure_type(self, i_distance_measure_type: CATOpnsMeasureDistanceType) -> 'MeasureBetween':  
        self.measure_between.SetDistanceMeasureType(int(i_distance_measure_type))
        return self

    def set_extension_mode(self, i_ref_extent_mode: CATOpnsMeasureExtensionMode, i_target_extent_mode: CATOpnsMeasureExtensionMode) -> 'MeasureBetween':
        self.measure_between.SetExtensionMode(int(i_ref_extent_mode), int(i_target_extent_mode))
        return self
    
    def set_first_selection(self, i_first_selections: list) -> 'MeasureBetween':
        self.measure_between.SetFirstSelection(i_first_selections)
        return self
    
    def set_result_computation_type(self, i_computation_type: CATResultCalcType) -> 'MeasureBetween': 
        self.measure_between.SetDistanceMeasureType(int(i_computation_type))
        return self
    
    def set_second_selection(self, i_second_selection: list) -> 'MeasureBetween': 
        self.measure_between.SetSecondSelection(i_second_selection)
        return self

    def set_selection_calculation_types(self, i_first_calculation_type: CATResultCalcType, i_second_calculation_type: CATResultCalcType) -> 'MeasureBetween':
        self.measure_between.SetSelectionCalculationTypes(int(i_first_calculation_type), int(i_second_calculation_type))
        return self    

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
