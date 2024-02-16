from typing import Iterator

from experience.inf_interfaces.viewer import Viewer
from experience.system.collection import Collection

class Viewers(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Viewers
    """

    def __init__(self, com):
        super().__init__(com, _child=Viewer)
        self.viewers = com

    def item(self, i_index: int) -> Viewer:
        return Viewer(self.viewers.Item(i_index))

    def __getitem__(self, n: int) -> Viewer:
        if (n + 1) > self.count():
            raise StopIteration

        return Viewer(self.viewers.item(n + 1))

    def __iter__(self) -> Iterator[Viewer]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Viewers(name="{self.name()}")'
