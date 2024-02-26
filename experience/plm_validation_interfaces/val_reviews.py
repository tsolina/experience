from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from experience.plm_validation_interfaces import VALReview

if TYPE_CHECKING:
    from experience.types import cat_variant

class VALReviews(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALReviews
    """
    def __init__(self, com):
        super().__init__(com, child=VALReview)
        self.val_reviews = com

    def add(self) -> VALReview:
        return VALReview(self.val_reviews.Add())

    def item(self, i_index: 'cat_variant') -> VALReview:
        return VALReview(self.val_reviews.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'VALReviews':
        self.val_reviews.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> VALReview:
        if (n + 1) > self.count():
            raise StopIteration
        return VALReview(self.val_reviews.item(n + 1))

    def __iter__(self) -> Iterator[VALReview]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))