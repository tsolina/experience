from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.inf_interfaces import Camera

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class Cameras(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Cameras
    """

    def __init__(self, com):
        super().__init__(com, child=Camera)
        self.cameras = com

    def item(self, i_index: 'cat_variant') -> 'Camera':
        return Camera(self.cameras.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'Cameras':
        self.cameras.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Camera:
        if (n + 1) > self.count:
            raise StopIteration

        return Camera(self.cameras.item(n + 1))

    def __iter__(self) -> Iterator[Camera]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Cameras(name="{self.name}")'
