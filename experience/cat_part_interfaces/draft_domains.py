from typing import Iterator, TYPE_CHECKING

from experience.cat_part_interfaces import DraftDomain
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types.general import cat_variant

class DraftDomains(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DraftDomains
    """

    def __init__(self, com):
        super().__init__(com)
        self.draft_domains = com

    def item(self, i_index: 'cat_variant') -> DraftDomain:
        return DraftDomain(self.draft_domains.Item(i_index))

    def __getitem__(self, n: int) -> DraftDomain:
        if (n + 1) > self.count:
            raise StopIteration

        return DraftDomain(self.draft_domains.item(n + 1))

    def __iter__(self) -> Iterator[DraftDomain]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'DraftDomains(name="{self.name}")'