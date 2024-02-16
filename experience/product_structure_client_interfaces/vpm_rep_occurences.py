from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.product_structure_client_interfaces import VPMRepOccurrence

if TYPE_CHECKING:
    from experience.types import cat_variant

class VPMRepOccurrences(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMRepOccurrences
    """

    def __init__(self, com):
        super().__init__(com, child=VPMRepOccurrence)
        self.vpm_rep_occurrences = com

    def item(self, i_index: 'cat_variant') -> VPMRepOccurrence:
        return VPMRepOccurrence(self.vpm_rep_occurrences.Item(i_index))

    def __getitem__(self, n: int) -> VPMRepOccurrence:
        if (n + 1) > self.count():
            raise StopIteration
        return VPMRepOccurrence(self.vpm_rep_occurrences.item(n + 1))

    def __iter__(self) -> Iterator[VPMRepOccurrence]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'VPMRepOccurrences(name="{self.name()}")'