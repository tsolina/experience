from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import KnowledgeCollection, KnowledgeFactory

class KnowledgeSet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.knowledge_set = com

    def collection(self) -> 'KnowledgeCollection':
        from experience.knowledge_interfaces import KnowledgeCollection
        return KnowledgeCollection(self.knowledge_set.Collection)

    def factory(self) -> 'KnowledgeFactory':
        from experience.knowledge_interfaces import KnowledgeFactory
        return KnowledgeFactory(self.knowledge_set.Factory)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'