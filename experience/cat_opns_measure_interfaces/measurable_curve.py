from experience.cat_opns_measure_interfaces import MeasurableInContext

class MeasurableCurve(MeasurableInContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         MeasurableCurve
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_curve = com

    def get_length(self) -> float:
        return self.measurable_curve.GetLength()
    
    def get_points(self) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
        return self._get_safe_array_multi(self.measurable_curve, "GetPoints", [2, 2, 2])

    def __repr__(self):
        return f'MeasurableCurve(name="{self.name()}")'
