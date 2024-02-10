from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_modeler_base_interfaces import PLMOccurrence

if TYPE_CHECKING:
    from experience.types import cat_variant

class PLMOccurrences(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMOccurrences
    """

    def __init__(self, com):
        super().__init__(com, child=PLMOccurrence)
        self.plm_occurrences = com

    def item(self, i_index: 'cat_variant') -> PLMOccurrence:
        return PLMOccurrence(self.printers.Item(i_index))

    def __getitem__(self, n: int) -> PLMOccurrence:
        if (n + 1) > self.count:
            raise StopIteration
        return PLMOccurrence(self.printers.item(n + 1))

    def __iter__(self) -> Iterator[PLMOccurrence]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'PLMOccurrence(name="{self.name}")'