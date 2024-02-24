from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_access_interfaces import PLMSearch

if TYPE_CHECKING:
    from experience.types import cat_variant

class PLMSearches(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMSearches
    """

    def __init__(self, com):
        super().__init__(com, child=PLMSearch)
        self.plm_searches = com

    def current(self, value: PLMSearch = None) -> PLMSearch:
        if value is not None:
            self._com.Current = value._com
            return self
        return PLMSearch(self.plm_searches.Current)

    def add(self) -> PLMSearch:
        return PLMSearch(self.plm_searches.Add)

    def item(self, i_index: 'cat_variant') -> PLMSearch:
        return PLMSearch(self.plm_searches.Item(i_index))

    def __getitem__(self, n: int) -> PLMSearch:
        if (n + 1) > self.count():
            raise StopIteration
        return PLMSearch(self.plm_searches.item(n + 1))

    def __iter__(self) -> Iterator[PLMSearch]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))