from typing import Union
from experience.knowledge_interfaces import Relation
from experience.knowledge_interfaces.knowledge_types import *

class Check(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Check
    """

    def __init__(self, com):
        super().__init__(com)
        self.check = com

    def diagnosis(self) -> bool:
        return self.check.Diagnosis
    
    def severity(self, value: KnowledgeSeverityType = None) -> Union['Check', KnowledgeSeverityType]:
        if value is not None:
            self.check.Severity = value.value
            return self
        return KnowledgeSeverityType.item(self.check.Severity) 

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'