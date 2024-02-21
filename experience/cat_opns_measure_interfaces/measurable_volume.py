from experience.cat_opns_measure_interfaces import MeasurableInContext

class MeasurableVolume(MeasurableInContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         MeasurableInContext
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_volume = com

    def get_area(self) -> float:
        return self.measurable_volume.GetArea()
    
    def get_cofg(self) -> tuple[float, float, float]:
        return self.measurable_volume.GetCOfG()
    
    def get_volume(self) -> float:
        return self.measurable_volume.GetVolume()
    
    def get_volume_area_cofg(self) -> tuple[float, float, float, float, float]:
        return self.measurable_volume.GetVolume_Area_COfG()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'