from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeSweep(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSweep
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_sweep = com

    def c0_vertices_mode(self, value: bool = None) -> Union['HybridShapeSweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep.C0VerticesMode = value
            return self
        return self.hybrid_shape_sweep.C0VerticesMode

    def fill_twisted_areas(self, value: int = None) -> Union['HybridShapeSweep', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep.FillTwistedAreas = value
            return self
        return self.hybrid_shape_sweep.FillTwistedAreas

    def setback_value(self, value: float = None) -> Union['HybridShapeSweep', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_sweep.SetbackValue = value
            return self
        return self.hybrid_shape_sweep.SetbackValue

    def add_cut_points(self, i_element1: Reference, i_element2: Reference) -> 'HybridShapeSweep':
        self.hybrid_shape_sweep.AddCutPoints(i_element1._com, i_element2._com)
        return self

    def add_fill_points(self, i_element1: Reference, i_element2: Reference) -> 'HybridShapeSweep':
        self.hybrid_shape_sweep.AddFillPoints(i_element1._com, i_element2._com)
        return self

    def get_cut_point(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_sweep.GetCutPoint(i_rank))

    def get_fill_point(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_sweep.GetFillPoint(i_rank))

    def remove_all_cut_points(self) -> 'HybridShapeSweep':
        self.hybrid_shape_sweep.RemoveAllCutPoints()
        return self

    def remove_all_fill_points(self) -> 'HybridShapeSweep':
        self.hybrid_shape_sweep.RemoveAllFillPoints()
        return self

    def __repr__(self):
        return f'HybridShapeSweep(name="{ self.name }")'