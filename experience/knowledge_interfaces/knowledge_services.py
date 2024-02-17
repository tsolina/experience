from typing import TYPE_CHECKING
from experience.inf_interfaces import Service
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Units, KnowledgeCollection
    from experience.knowledge_interfaces.knowledge_types import *


class KnowledgeServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         KnowledgeServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.knowledge_services = com
    
    def units(self) -> 'Units':
        from experience.knowledge_interfaces import Units
        return self.knowledge_services.Units()   

    def get_knowledge_collection(self, i_root: AnyObject, ik_set_type: 'KnowledgeSetType') -> 'KnowledgeCollection':
        from experience.knowledge_interfaces import KnowledgeCollection
        return KnowledgeCollection(self.knowledge_services.GetKnowledgeCollection(i_root._com, ik_set_type.value))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'