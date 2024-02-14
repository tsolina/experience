from experience.cat_opns_measure_interfaces import MeasurableInContext

class MeasurablePoint(MeasurableInContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         MeasurablePoint
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_point = com

    def get_point(self) -> tuple[float, float, float]:
        return self.measurable_point.GetPoint()
    
    def __repr__(self):
        return f'MeasurablePoint(name="{self.name()}")'
