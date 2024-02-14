from experience.cat_opns_measure_interfaces import MeasurableCurve

class MeasurableSurface(MeasurableCurve):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableInContext
                |                             MeasurableSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_surface = com

    def get_area(self) -> float:
        return self.measurable_surface.GetArea()
    
    def get_area_cofg(self) -> tuple[float, float, float, float]:
        return self.measurable_surface.GetArea_COfG() # - to check if they have to be returned differently
    
    def get_cofg(self) -> tuple[float, float, float]:
        return self.measurable_surface.GetCOfG()
    
    def get_perimeter(self) -> float:
        return self.measurable_surface.GetPerimeter()

    def __repr__(self):
        return f'MeasurableSurface(name="{self.name()}")'
