from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.product_structure_client_interfaces import VPMOccurrence

if TYPE_CHECKING:
    from experience.types import cat_variant

class VPMOccurrences(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMOccurrences
    """

    def __init__(self, com):
        super().__init__(com, child=VPMOccurrence)
        self.vpm_occurrences = com

    def item(self, i_index: 'cat_variant') -> VPMOccurrence:
        return VPMOccurrence(self.vpm_occurrences.Item(i_index))

    def __getitem__(self, n: int) -> VPMOccurrence:
        if (n + 1) > self.count:
            raise StopIteration
        return VPMOccurrence(self.vpm_occurrences.item(n + 1))

    def __iter__(self) -> Iterator[VPMOccurrence]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'VPMOccurrences(name="{self.name()}")'