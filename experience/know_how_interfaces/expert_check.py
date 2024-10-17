from typing import Union, TYPE_CHECKING

from experience.know_how_interfaces.expert_check_runtime import ExpertCheckRuntime

if TYPE_CHECKING:
    from experience.know_how_interfaces.expert_check import ExpertRule

class ExpertCheck(ExpertCheckRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                         KnowHowIDLItf.ExpertCheckRuntime
                |                             ExpertCheck
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_check = com

    def body(self, value: str = None) -> Union['ExpertCheck', str]:
        if value is not None:
            self.expert_check.Body = value
            return self
        return self.expert_check.Body
    
    def language(self, value: int = None) -> Union['ExpertCheck', int]:
        if value is not None:
            self.expert_check.Language = value
            return self
        return self.expert_check.Language
    
    def variables(self, value: str = None) -> Union['ExpertCheck', str]:
        if value is not None:
            self.expert_check.Variables = value
            return self
        return self.expert_check.Variables

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'