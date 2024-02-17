from typing import TYPE_CHECKING
from experience.system.any_object import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import KnowledgeCollection

class KnowledgeFactory(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.knowledge_factory = com

    def collection(self) -> 'KnowledgeCollection':
        from experience.knowledge_interfaces import KnowledgeCollection
        return KnowledgeCollection(self.knowledge_factory.Collection)

    def root(self) -> AnyObject:
        return AnyObject(self.knowledge_factory.Root)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
