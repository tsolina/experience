from typing import TYPE_CHECKING
from experience.system import AnyObject
from experience.knowledge_interfaces import KnowledgeServices

if TYPE_CHECKING:
    from experience.knowledge_interfaces import KnowledgeSet 
    from experience.knowledge_interfaces.knowledge_types import *


class KnowledgeObjects(KnowledgeServices):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         KnowledgeIDLItf.KnowledgeServices
                |                             KnowledgeObjects

    """

    def __init__(self, com):
        super().__init__(com)
        self.knowledge_objects = com

    def get_knowledge_root_set(self, i_create_or_not: AnyObject, ik_set_type: 'KnowledgeSetType') -> 'KnowledgeSet':
        from experience.knowledge_interfaces import KnowledgeSet
        return KnowledgeSet(self.knowledge_services.GetKnowledgeRootSet(i_create_or_not, ik_set_type.value))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'