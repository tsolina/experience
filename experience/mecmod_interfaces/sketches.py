from typing import Iterator

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Boundary
from experience.system import Collection
from experience.types import cat_variant

class Sketches(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Sketches
    """

    def __init__(self, com):
        super().__init__(com, child=None)  # Note: Initialize _child as None initially
        self.sketches = com

    def add(self, i_plane: Reference):
        from experience.cat_sketcher_interfaces import Sketch  # Import Sketch locally
        return Sketch(self.sketches.Add(i_plane._com))

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.sketches.GetBoundary(i_label))

    def item(self, i_index: cat_variant):
        from experience.cat_sketcher_interfaces import Sketch  # Import Sketch locally
        return Sketch(self.sketches.Item(i_index))

    def __getitem__(self, n: int):
        if (n + 1) > self.count():
            raise StopIteration
        from experience.cat_sketcher_interfaces import Sketch  # Import Sketch locally
        return Sketch(self.sketches.item(n + 1))

    def __iter__(self) -> Iterator:
        for i in range(self.count()):
            from experience.cat_sketcher_interfaces import Sketch  # Import Sketch locally
            yield Sketch(self._com.item(i + 1))