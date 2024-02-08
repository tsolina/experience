from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces.hybrid_shape import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces.length import Length

class HybridShapePolyline(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapePolyline
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_polyline = com

    def closure(self, value: bool = None) -> Union['HybridShapePolyline', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_polyline.Closure = value
            return self
        return self.hybrid_shape_polyline.Closure

    def number_of_elements(self) -> int:
        return self.hybrid_shape_polyline.NumberOfElements

    def get_element(self, i_position: int) -> None:
        return self.hybrid_shape_polyline.GetElement(i_position)

    def insert_element(self, i_point: Reference, i_position: int) -> 'HybridShapePolyline':
        self.hybrid_shape_polyline.InsertElement(i_point._com, i_position)
        return self

    def remove_element(self, i_position: int) -> 'HybridShapePolyline':
        self.hybrid_shape_polyline.RemoveElement(i_position)
        return self

    def replace_element(self, i_point: Reference, i_position: int) -> 'HybridShapePolyline':
        self.hybrid_shape_polyline.ReplaceElement(i_point._com, i_position)
        return self

    def set_radius(self, i_position: int, i_radius: float) -> 'HybridShapePolyline':
        self.hybrid_shape_polyline.SetRadius(i_position, i_radius)
        return self

    def __repr__(self):
        return f'HybridShapePolyline(name="{self.name}")'