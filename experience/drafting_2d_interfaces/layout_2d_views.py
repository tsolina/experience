from typing import Iterator, TYPE_CHECKING

from experience.drafting_2d_interfaces.drafting_2d_types import *

from .layout_2d_view import Layout2DView
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class Layout2DViews(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Layout2DViews
    """

    def __init__(self, com):
        super().__init__(com, child=Layout2DView)
        self.layout_2d_views = com

    def active_view(self) -> Layout2DView:
        return Layout2DView(self.layout_2d_views.ActiveView)

    def add_auxiliary(self, i_reference_view: Layout2DView, i_bc_segment: list, i_x_orient: float, i_y_orient: float, i_section_type: CatViewType, i_x: float, i_y: float):
        return Layout2DView(self.layout_2d_views.AddAuxiliary(i_reference_view._com, i_bc_segment, i_x_orient, i_y_orient, i_section_type, i_x, i_y))
    
    def add_detail(self, i_detail_name: str) -> Layout2DView:
        return Layout2DView(self.layout_2d_views.AddDetail(i_detail_name))
    
    def add_from_3d_plane(self, i_plane: list, i_view_type: CatViewType, i_x: float, i_y: float):
        return Layout2DView(self.layout_2d_views.AddFrom3DPlane(i_plane, i_view_type, i_x, i_y))
    
    def add_primary(self, i_x: float, i_y: float):
        return Layout2DView(self.layout_2d_views.AddPrimary(i_x, i_y))
    
    def add_related(self, i_reference_view: Layout2DView, i_side: CatViewSide, i_x: float, i_y: float):
        return Layout2DView(self.layout_2d_views.AddRelated(i_reference_view._com, i_side, i_x, i_y))

    def item(self, i_index: 'cat_variant') -> Layout2DView:
        return Layout2DView(self.layout_2d_views.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'Layout2DViews':
        self.layout_2d_views.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Layout2DView:
        if (n + 1) > self.count():
            raise StopIteration

        return Layout2DView(self.layout_2d_views.item(n + 1))

    def __iter__(self) -> Iterator[Layout2DView]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
