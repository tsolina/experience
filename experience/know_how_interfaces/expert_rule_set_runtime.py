from typing import TYPE_CHECKING
from experience.know_how_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

if TYPE_CHECKING:
    from experience.know_how_interfaces import ExpertRuleBaseComponentRuntimes, ExpertRuleSet

class ExpertRuleSetRuntime(ExpertRuleBaseComponentRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                       ExpertRuleSetRuntime
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_set_runtime = com

    def expert_rule_base_component_runtimes(self) -> 'ExpertRuleBaseComponentRuntimes':
        from experience.know_how_interfaces.expert_rule_base_component_runtimes import ExpertRuleBaseComponentRuntimes
        return ExpertRuleBaseComponentRuntimes(self.expert_rule_set_runtime.ExpertRuleBaseComponentRuntimes)
    
    def rule_set_edition(self) -> 'ExpertRuleSet':
        from experience.know_how_interfaces.expert_rule_set import ExpertRuleSet
        return ExpertRuleSet(self.expert_rule_set_runtime.RuleSetEdition)
    
    def status(self) -> int:
        return self.expert_rule_set_runtime.Status()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'