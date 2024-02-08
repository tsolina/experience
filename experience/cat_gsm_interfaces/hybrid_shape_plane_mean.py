from typing import Union, Optional, TYPE_CHECKING

from experience.cat_gsm_interfaces import Plane
from experience.inf_interfaces import Reference

class HybridShapePlaneMean(Plane):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneMean
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_plane_mean = com

    def add_point(self, i_passing_point: Reference) -> 'HybridShapePlaneMean':
        self.hybrid_shape_plane_mean.AddPoint(i_passing_point._com)
        return self

    def get_point(self, i_rank: int, o_passing_point: Reference) -> 'HybridShapePlaneMean':
        self.hybrid_shape_plane_mean.GetPoint(i_rank, o_passing_point._com)
        return self

    def get_pos(self, i_point: Reference) -> int:
        return self.hybrid_shape_plane_mean.GetPos(i_point.com)

    def get_size(self) -> int:
        return self.hybrid_shape_plane_mean.GetSize()

    def remove_all(self) -> 'HybridShapePlaneMean':
        self.hybrid_shape_plane_mean.RemoveAll()
        return self

    def remove_element(self, i_rank: int) -> 'HybridShapePlaneMean':
        self.hybrid_shape_plane_mean.RemoveElement(i_rank)
        return self

    def replace_point_at_position(self, i_point: Reference, i_pos: int) -> 'HybridShapePlaneMean':
        self.hybrid_shape_plane_mean.ReplacePointAtPosition(i_point.com, i_pos)
        return self

    def __repr__(self):
        return f'HybridShapePlaneMean(name="{self.name}")'