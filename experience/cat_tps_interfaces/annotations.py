from typing import Iterator

from experience.system import AnyObject, Collection
from experience.cat_tps_interfaces import Annotation
from experience.types import cat_variant

class Annotations(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Annotations
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotations = com
        self._child = Annotation

    def add(self, i_annot: Annotation) -> None:
        return self.annotations.Add(i_annot._com)

    def item(self, i_index: cat_variant) -> Annotation:
        return Annotation(self.annotations.Item2(i_index))

    def item2(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.annotations.Item2(i_index))

    def __getitem__(self, n: int) -> Annotation:
        if (n + 1) > self.count():
            raise StopIteration

        return Annotation(self.annotations.item(n + 1))

    def __iter__(self) -> Iterator[Annotation]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Annotations(name="{self.name()}")'
