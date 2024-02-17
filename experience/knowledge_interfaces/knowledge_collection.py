from typing import Iterator, TYPE_CHECKING

from experience.system import Collection, AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.knowledge_interfaces import KnowledgeFactory
    from experience.knowledge_interfaces.knowledge_types import *

class KnowledgeCollection(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KnowledgeCollection
    """

    def __init__(self, com):
        super().__init__(com, child=AnyObject)
        self.knowledge_collection = com

    def factory(self) -> 'KnowledgeFactory':
        from experience.knowledge_interfaces import KnowledgeFactory
        return KnowledgeFactory(self.knowledge_collection.Factory)

    def find(self, i_object_type: 'KnowledgeObjectType', i_recursively: bool) -> 'KnowledgeCollection':
        return KnowledgeCollection(self.knowledge_collection.Find(i_object_type.value, i_recursively))

    def item(self, i_index: int) -> AnyObject:
        return AnyObject(self.knowledge_collection.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'KnowledgeCollection':
        self.knowledge_collection.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count():
            raise StopIteration

        return AnyObject(self.knowledge_collection.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
