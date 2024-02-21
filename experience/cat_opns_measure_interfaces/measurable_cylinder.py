from experience.cat_opns_measure_interfaces import MeasurableSurface

class MeasurableCylinder(MeasurableSurface):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableSurface
                |                             MeasurableCylinder
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_cylinder = com

    def get_axis(self) -> tuple[float, float, float]:
        return self.measurable_cylinder.GetAxis() # - to check if they have to be returned differently
    
    def get_point(self) -> tuple[float, float, float]:
        return self.measurable_cylinder.GetPoint()
    
    def get_points(self) -> tuple[float, float, float, float, float, float]:
        return self.measurable_cylinder.GetPoints()
    
    def get_radius(self) -> float:
        return self.measurable_cylinder.GetRadius()    

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
