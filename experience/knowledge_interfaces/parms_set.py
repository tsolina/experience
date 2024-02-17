from typing import TYPE_CHECKING
from experience.system import AnyObject

from experience.knowledge_interfaces import KnowledgeSet

class ParmsSet(KnowledgeSet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeSet
                |                         ParmsSet   
    """

    def __init__(self, com):
        super().__init__(com)
        self.parms_set = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'