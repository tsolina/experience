from typing import Iterator, TYPE_CHECKING

from .expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class ExpertRuleBaseComponentRuntimes(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertRuleBaseComponentRuntimes
    """

    def __init__(self, com):
        super().__init__(com, child=ExpertRuleBaseComponentRuntime)
        self.expert_rule_base_component_runtimes = com

    def item(self, i_index: 'cat_variant') -> ExpertRuleBaseComponentRuntime:
        return ExpertRuleBaseComponentRuntime(self.expert_rule_base_component_runtimes.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'ExpertRuleBaseComponentRuntimes':
        self.expert_rule_base_component_runtimes.Remove(i_index)
        return self
    
    def shallow_count(self) -> int:
        return self.expert_rule_base_component_runtimes.ShallowCount()
    
    def shallow_item(self, i_index: 'cat_variant') -> ExpertRuleBaseComponentRuntime:
        return ExpertRuleBaseComponentRuntime(self.expert_rule_base_component_runtimes.ShallowItem(i_index))
    
    def shallow_remove(self, i_index: 'cat_variant') -> 'ExpertRuleBaseComponentRuntimes':
        self.expert_rule_base_component_runtimes.ShallowRemove(i_index)
        return self

    def __getitem__(self, n: int) -> ExpertRuleBaseComponentRuntime:
        if (n + 1) > self.count():
            raise StopIteration

        return ExpertRuleBaseComponentRuntime(self.expert_rule_base_component_runtimes.item(n + 1))

    def __iter__(self) -> Iterator[ExpertRuleBaseComponentRuntime]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
