from typing import Iterator, TYPE_CHECKING

from experience.cat_part_interfaces import DefeaturingFilter
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant


class DefeaturingFilters(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DefeaturingFilters
    """

    def __init__(self, com):
        super().__init__(com)
        self.defeaturing_filters = com

    def add(self, i_filter_type_to_add: str) -> int:
        return self.defeaturing_filters.Add(i_filter_type_to_add)

    def item(self, i_filter_id: 'cat_variant') -> DefeaturingFilter:
        return DefeaturingFilter(self.defeaturing_filters.Item(i_filter_id))

    def remove(self, i_filter_id: 'cat_variant') -> 'DefeaturingFilters':
        self.defeaturing_filters.Remove(i_filter_id)
        return self

    def __getitem__(self, n: int) -> DefeaturingFilter:
        if (n + 1) > self.count():
            raise StopIteration

        return DefeaturingFilter(self.defeaturing_filters.item(n + 1))

    def __iter__(self) -> Iterator[DefeaturingFilter]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'