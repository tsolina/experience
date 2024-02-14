from experience.cat_opns_measure_interfaces import MeasurableSurface

class MeasurableSphere(MeasurableSurface):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableSurface
                |                             MeasurableSphere
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_sphere = com
    
    def get_center(self) -> tuple[float, float, float]:
        return self.measurable_sphere.GetCenter() # - to check if they have to be returned differently
    
    def get_radius(self) -> float:
        return self.measurable_sphere.GetRadius()

    def __repr__(self):
        return f'MeasurableSphere(name="{self.name()}")'
