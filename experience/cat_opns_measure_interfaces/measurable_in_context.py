from experience.system import AnyObject
from experience.cat_opns_measure_interfaces.opns_measure_types import *

class MeasurableInContext(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MeasurableInContext
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_in_context = com

    def get_axis_system_from_measurable(self) -> tuple:
        return self._get_safe_array(self.measurable_in_context, "GetAxisSystemFromMeasurable", 11)
    
    def get_result_computation_mode(self) -> CATMeasurableModeOfCalc:
        return CATMeasurableModeOfCalc.item(self.measurable_in_context.GetResultComputationMode())

    def get_result_computation_type(self) -> CATResultCalcType:
        return CATResultCalcType.item(self.measurable_in_context.GetResultComputationType())
    
    def set_axis_system_on_measurable(self, i_axis_positioning: list) -> 'MeasurableInContext':
        """ - tuple of 12 floats - """
        self.measurable_in_context.SetAxisSystemOnMeasurable(i_axis_positioning)
        return self
    
    def set_measurable_context_type(self, i_context_type: CATMeasurableContextType) -> 'MeasurableInContext':
        self.measurable_in_context.SetMeasurableContextType(int(i_context_type))
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'