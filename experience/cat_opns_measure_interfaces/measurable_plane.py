from experience.cat_opns_measure_interfaces import MeasurableSurface

class MeasurablePlane(MeasurableSurface):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         CATOpnsMeasureIDLItf.MeasurableSurface
                |                             MeasurablePlane
    """

    def __init__(self, com):
        super().__init__(com)
        self.measurable_plane = com
    
    def get_plane(self) -> tuple[float, float, float, float, float, float, float, float, float]:
        return self._get_safe_array(self.measurable_plane, "GetPlane", 8)

    def __repr__(self):
        return f'MeasurablePlane(name="{self.name()}")'
