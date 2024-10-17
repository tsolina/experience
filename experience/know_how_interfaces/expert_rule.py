from typing import Union, TYPE_CHECKING

from experience.know_how_interfaces.expert_rule_runtime import ExpertRuleRuntime

if TYPE_CHECKING:
    from experience.know_how_interfaces.expert_rule import ExpertRule

class ExpertRule(ExpertRuleRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                         KnowHowIDLItf.ExpertRuleRuntime
                |                             ExpertRule
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule = com

    def body(self, value: str = None) -> Union['ExpertRule', str]:
        if value is not None:
            self.expert_rule.Body = value
            return self
        return self.expert_rule.Body
    
    def language(self, value: int = None) -> Union['ExpertRule', int]:
        if value is not None:
            self.expert_rule.Language = value
            return self
        return self.expert_rule.Language
    
    def variables(self, value: str = None) -> Union['ExpertRule', str]:
        if value is not None:
            self.expert_rule.Variables = value
            return self
        return self.expert_rule.Variables

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'