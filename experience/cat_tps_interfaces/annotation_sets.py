from typing import Iterator

# from experience.product_structure.product import Product    # TODO:
from experience.system import AnyObject, Collection
from experience.cat_tps_interfaces import AnnotationSet
from experience.types.general import cat_variant

class AnnotationSets(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnnotationSets
    """

    def __init__(self, com):
        super().__init__(com)
        self.annotation_sets = com
        self._child = AnnotationSet

    # def add_in_a_product(self, i_product: Product, i_standard: str) -> AnnotationSet:
    #     return AnnotationSet(self.annotation_sets.AddInAProduct(i_product._com, i_standard))

    def item(self, i_index: cat_variant) -> AnnotationSet:
        return AnnotationSet(self.annotation_sets.Item(i_index))

    def load_annotation_sets_list(self) -> None:
        return self.annotation_sets.LoadAnnotationSetsList()

    def __getitem__(self, n: int) -> AnnotationSet:
        if (n + 1) > self.count:
            raise StopIteration

        return AnnotationSet(self.annotation_sets.item(n + 1))

    def __iter__(self) -> Iterator[AnnotationSet]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))