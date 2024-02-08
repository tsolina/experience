from typing import Iterator

from experience.cat_annotation_interfaces import DrawingDimension
from experience.system import Collection
from experience.types import cat_variant


class DrawingDimensions(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingDimensions
    """

    def __init__(self, com):
        super().__init__(com, _child=DrawingDimension)
        self.drawing_dimensions = com

    def add(self, i_type_dim: int, i_geom_elem: tuple, i_pt_coord_elem: tuple, i_line_rep: int) -> DrawingDimension:
        return DrawingDimension(self.drawing_dimensions.Add(i_type_dim, i_geom_elem, i_pt_coord_elem, i_line_rep))

    def add2(self, i_type_dim: int, i_geom_elem: tuple, i_pt_coord_elem: tuple, i_ldc_ref_elem: cat_variant, i_ldc_ref_angle: int) -> DrawingDimension:
        return DrawingDimension(self.drawing_dimensions.Add2(i_type_dim, i_geom_elem, i_pt_coord_elem, i_ldc_ref_elem, i_ldc_ref_angle))

    def item(self, i_index: cat_variant) -> DrawingDimension:
        return DrawingDimension(self.drawing_dimensions.Item(i_index))

    def remove(self, i_index: cat_variant) -> 'DrawingDimensions':
        self.drawing_dimensions.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> DrawingDimension:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingDimension(self.drawing_dimensions.item(n + 1))

    def __iter__(self) -> Iterator[DrawingDimension]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DrawingDimensions(name="{self.name}")'
