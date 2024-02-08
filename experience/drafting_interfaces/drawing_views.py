from typing import Iterator

from experience.types import cat_variant
from experience.drafting_interfaces import DrawingView
from experience.system import AnyObject, Collection

class DrawingViews(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingViews
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingView)
        self.drawing_views = com


    def active_view(self) -> DrawingView:
        return DrawingView(self.drawing_views.ActiveView)


    def drawing_define_gen_view(self) -> AnyObject:
        return AnyObject(self.drawing_views.DrawingDefineGenView)

    def add(self, i_drawing_view_name: str) -> DrawingView:
        return DrawingView(self.drawing_views.Add(i_drawing_view_name))

    def add_front_view(self, i_x_pt_1: float, i_y_pt_1: float, i_drawing_view_name: str, i_x_1: float, i_y_1: float, i_z_1: float, i_x_2: float, i_y_2: float, i_z_2: float) -> 'DrawingView':
        return DrawingView(self.drawing_views.AddFrontView(i_x_pt_1, i_y_pt_1, i_drawing_view_name, i_x_1, i_y_1, i_z_1, i_x_2, i_y_2, i_z_2))

    def add_isometric_view(self, i_x_pt_1: float, i_y_pt_1: float, i_drawing_view_name: str, i_x_1: float, i_y_1: float, i_z_1: float, i_x_2: float, i_y_2: float, i_z_2: float) -> 'DrawingView':
        return DrawingView(self.drawing_views.AddIsometricView(i_x_pt_1, i_y_pt_1, i_drawing_view_name, i_x_1, i_y_1, i_z_1, i_x_2, i_y_2, i_z_2))

    def add_projection_view(self, i_x_pt_1: float, i_y_pt_1: float, i_drawing_view_name: str, i_parent_view: 'DrawingView', i_type: int) -> 'DrawingView':
        return DrawingView(self.drawing_views.AddProjectionView(i_x_pt_1, i_y_pt_1, i_drawing_view_name, i_parent_view, i_type))

    def item(self, i_index: cat_variant) -> DrawingView:
        return DrawingView(self.drawing_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> 'DrawingViews':
        self.drawing_views.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingView:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingView(self.drawing_views.item(n + 1))

    def __iter__(self) -> Iterator[DrawingView]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingViews(name="{self.name}")'
