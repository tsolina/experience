from typing import Union
from experience.system import AnyObject

class ExpertRuleBaseComponentRuntime(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertRuleBaseComponentRuntime
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_base_component_runtime = com

    def comment(self, value: str = None) -> Union['ExpertRuleBaseComponentRuntime', str]:
        if value is not None:
            self.expert_rule_base_component_runtime.Comment = value
            return self
        return self.expert_rule_base_component_runtime.Comment
    
    def accurate_type(self) -> str:
        return self.expert_rule_base_component_runtime.AccurateType()
    
    def activate(self) -> 'ExpertRuleBaseComponentRuntime':
        self.expert_rule_base_component_runtime.Activate()
        return self

    def deactivate(self) -> 'ExpertRuleBaseComponentRuntime':
        self.expert_rule_base_component_runtime.Deactivate()
        return self
    
    def is_use_only(self) -> bool:
        return self.expert_rule_base_component_runtime.IsUseOnly()
    
    def is_activate(self) -> bool:
        return self.expert_rule_base_component_runtime.Isactivate()
    
    def parse(self) -> str:
        return self.expert_rule_base_component_runtime.Parse()
    
    def set_use_only(self) -> 'ExpertRuleBaseComponentRuntime':
        self.expert_rule_base_component_runtime.SetUseOnly()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'