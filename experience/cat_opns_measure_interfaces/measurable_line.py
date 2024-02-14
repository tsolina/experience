from experience.cat_opns_measure_interfaces import MeasurableCurve

class MeasurableLine(MeasurableCurve):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableCurve
                |                             MeasurableLine
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_line = com
    
    def get_direction(self) -> tuple[float, float, float]:
        return self.measurable_curve.GetDirection() # - to check if they have to be returned differently
    
    def get_origin(self) -> tuple[float, float, float]:
        return self.measurable_curve.GetOrigin()

    def __repr__(self):
        return f'MeasurableLine(name="{self.name()}")'
