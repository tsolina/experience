from typing import Iterator

from experience.system import AnyObject, Collection
from experience.types import cat_variant
from experience.cat_tps_interfaces import TPSView

class TPSViews(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     TPSViews
    """

    def __init__(self, com):
        super().__init__(com)
        self.tps_views = com
        self._child = TPSView

    def item(self, i_index: cat_variant) -> TPSView:
        return TPSView(self.tps_views.Item(i_index))

    def __getitem__(self, n: int) -> TPSView:
        if (n + 1) > self.count():
            raise StopIteration

        return TPSView(self.tps_views.item(n + 1))

    def __iter__(self) -> Iterator[TPSView]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))