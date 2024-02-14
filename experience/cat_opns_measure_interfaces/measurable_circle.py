from experience.cat_opns_measure_interfaces import MeasurableCurve

class MeasurableCircle(MeasurableCurve):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableCurve
                |                             MeasurableCircle
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_circle = com

    def get_angle(self) -> float:
        return self.measurable_circle.GetAngle()
    
    def get_axis(self) -> tuple[float, float, float]:
        return self.measurable_circle.GetAxis() # - to check if they have to be returned differently
    
    def get_center(self) -> tuple[float, float, float]:
        return self.measurable_circle.GetCenter()
    
    def get_radius(self) -> float:
        return self.measurable_circle.GetRadius()

    def __repr__(self):
        return f'MeasurableCircle(name="{self.name()}")'
