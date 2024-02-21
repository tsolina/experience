from experience.cat_opns_measure_interfaces import MeasurableSurface

class MeasurableCone(MeasurableSurface):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableSurface
                |                             MeasurableCone
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_cone = com

    def get_angle(self) -> float:
        return self.measurable_cone.GetAngle()
    
    def get_axis(self) -> tuple[float, float, float]:
        return self.measurable_cone.GetAxis() # - to check if they have to be returned differently
    
    def get_point(self) -> tuple[float, float, float]:
        return self.measurable_cone.GetPoint()
    
    def get_points(self) -> tuple[float, float, float, float, float, float]:
        return self.measurable_cone.GetPoints()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'