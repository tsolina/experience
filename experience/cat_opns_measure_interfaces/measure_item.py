from experience.system import AnyObject
from experience.cat_opns_measure_interfaces.opns_measure_types import *

class MeasureItem(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MeasureItem
    """

    def __init__(self, com):
        super().__init__(com)
        self.measure_item = com

    def get_angle(self) -> float:
        return self.measure_item.GetAngle()
    
    def get_area(self) -> float:
        return self.measure_item.GetArea()
    
    def get_axis(self) -> tuple[float, float, float]:
        return self.measure_item.GetAxis()
    
    def get_axis_system_from_measure(self) -> tuple[float, float, float, float, float, float, float, float, float, float, float, float]:
        return self._get_safe_array(self.measure_item, "GetAxisSystemFromMeasure", 11)
    
    def get_cofg(self) -> tuple[float, float, float]:
        return self.measure_item.GetCOfG()
    
    def get_center(self) -> tuple[float, float, float]:
        return self.measure_item.GetCenter()
    
    def get_computation_mode(self) -> CATMeasurableModeOfCalc:
        return CATMeasurableModeOfCalc.item(self.measure_item.GetComputationMode())
    
    def get_curve_points(self) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
        return self._get_safe_array_multi(self.measure_item, "GetCurvePoints", [2, 2, 2])

    def get_direction(self) -> tuple[float, float, float]:
        return self.measure_item.GetDirection()    
    
    def get_length(self) -> float:
        return self.measure_item.GetLength()
    
    def get_measure_edge_type(self) -> CATOpnsMeasureEdgeType:
        return CATOpnsMeasureEdgeType.item(self.measure_item.GetMeasureEdgeType())
    
    def get_measure_item_type(self) -> CATOpnsMeasureItemType:
        return CATOpnsMeasureItemType.item(self.measure_item.GetMeasureItemType())   

    def get_measure_surface_type(self) -> CATOpnsMeasureSurfaceType:
        return CATOpnsMeasureSurfaceType.item(self.measure_item.GetMeasureSurfaceType())   

    def get_origin(self) -> tuple[float, float, float]:
        return self.measure_item.GetOrigin()
    
    def get_perimeter(self) -> float:
        return self.measure_item.GetPerimeter()
    
    def get_plane(self) -> tuple[float, float, float, float, float, float, float, float, float]:
        return self._get_safe_array(self.measure_item, "GetPlane", 8)
    
    def get_point(self) -> tuple[float, float, float]:
        return self.measure_item.GetPoint()
    
    def get_points(self) -> tuple[float, float, float, float, float, float]:
        return self.measure_item.GetPoint()
    
    def get_radius(self) -> float:
        return self.measure_item.GetRadius()
    
    def get_result_calculation_type(self) -> CATResultCalcType:
        return CATResultCalcType.item(self.measure_item.GetResultComputationType())  
    
    def get_selection(self) -> tuple:
        return self._get_safe_array(self.measure_item, "GetSelection", "")
    
    def get_volume(self) -> float:
        return self.measure_item.GetVolume()   
    
    def get_volume_area_cofg(self) -> tuple[float, float, float, float, float]:
        return self.measure_item.GetVolume_Area_COfG()
    
    def set_axis_system_on_measure(self, i_axis_positioning: tuple) -> 'MeasureItem':
        self.measure_item.SetAxisSystemOnMeasure(i_axis_positioning)
        return self
    
    def set_computation_mode(self, i_computation_mode: CATMeasurableModeOfCalc) -> 'MeasureItem':
        self.measure_item.SetComputationMode(int(i_computation_mode))
        return self

    def set_measure_item_type(self, i_measure_item_type: CATOpnsMeasureItemType) -> 'MeasureItem':
        self.measure_item.SetMeasureItemType(int(i_measure_item_type))
        return self
    
    def set_selection(self, i_selections: tuple) -> 'MeasureItem':
        self.measure_item.SetSelection(i_selections)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'