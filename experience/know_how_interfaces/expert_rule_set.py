from typing import TYPE_CHECKING

from experience.know_how_interfaces.expert_rule_set_runtime import ExpertRuleSetRuntime

if TYPE_CHECKING:
    from experience.know_how_interfaces import ExpertCheck, ExpertRule

class ExpertRuleSet(ExpertRuleSetRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                       KnowHowIDLItf.ExpertRuleSetRuntime
                |                           ExpertRuleSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_set = com

    def create_check(self, i_name: str, i_check_variables: str, i_check_body: str, i_rule_set: str) -> 'ExpertCheck':
        from experience.know_how_interfaces.expert_check import ExpertCheck
        return ExpertCheck(self.expert_rule_set.CreateCheck(i_name, i_check_variables, i_check_body, i_rule_set))
    
    def create_rule(self, i_name: str, i_rule_variables: str, i_rule_body: str, i_rule_set: str) -> 'ExpertRule':
        from experience.know_how_interfaces import ExpertRule
        return ExpertRule(self.expert_rule_set.CreateRule(i_name, i_rule_variables, i_rule_body, i_rule_set))
    
    def create_rule_set(self, i_name: str, i_rule_set: str) -> 'ExpertRuleSet':
        return ExpertRuleSet(self.expert_rule_set.CreateRuleSet(i_name, i_rule_set))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'