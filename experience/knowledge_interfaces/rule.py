from typing import Union
from experience.knowledge_interfaces import Relation
from experience.knowledge_interfaces.knowledge_types import *

class Rule(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Rule
    """

    def __init__(self, com):
        super().__init__(com)
        self.rule = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'