from experience.cat_opns_measure_interfaces import MeasurableInContext

class MeasurableAxisSystem(MeasurableInContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext.MeasurableInContext
                |                         MeasurableAxisSystem
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_axis_system = com

    def get_axis(self) -> tuple: # 12
        return self._get_safe_array(self.measurable_axis_system, "GetAxis", 11)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
