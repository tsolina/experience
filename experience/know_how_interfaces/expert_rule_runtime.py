from typing import Union, TYPE_CHECKING

from experience.know_how_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

if TYPE_CHECKING:
    from experience.know_how_interfaces.expert_rule import ExpertRule

class ExpertRuleRuntime(ExpertRuleBaseComponentRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                         ExpertRuleRuntime
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_runtime = com

    def priority(self, value: float = None) -> Union['ExpertRuleRuntime', float]:
        if value is not None:
            self.expert_rule_runtime.Priority = value
            return self
        return self.expert_rule_runtime.Priority
    
    def rule_edition(self) -> 'ExpertRule':
        from experience.know_how_interfaces.expert_rule import ExpertRule
        return ExpertRule(self.expert_rule_runtime.RuleEdition)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'