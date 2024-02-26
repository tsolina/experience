from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_validation_interfaces import Marker

if TYPE_CHECKING:
    from experience.types import cat_variant

class Markers(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Markers
    """
    # Dim cMarkers As Markers 
    # Set cMarkers = TheVALReview.GetFactory("Markers")

    def __init__(self, com):
        super().__init__(com, child=Marker)
        self.markers = com

    def add(self, i_text: str) -> Marker:
        return Marker(self.markers.Add(i_text))
    
    def add_shape(self, i_coordinates: tuple, i_text: str) -> Marker:
        return Marker(self.markers.AddShape(i_coordinates, i_text))

    def item(self, i_index: 'cat_variant') -> Marker:
        return Marker(self.markers.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'Markers':
        self.markers.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> Marker:
        if (n + 1) > self.count():
            raise StopIteration
        return Marker(self.markers.item(n + 1))

    def __iter__(self) -> Iterator[Marker]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))