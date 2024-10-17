from typing import TYPE_CHECKING
from experience.knowledge_interfaces.knowledge_factory import KnowledgeFactory

if TYPE_CHECKING:
    from experience.know_how_interfaces.expert_rule_base import ExpertRuleBase

class ExpertRuleBasesFactory(KnowledgeFactory):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         ExpertRuleBasesFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_bases_factory = com

    def create_rule_base(self, i_name: str) -> 'ExpertRuleBase':
        from experience.know_how_interfaces.expert_rule_base import ExpertRuleBase
        return ExpertRuleBase(self.expert_rule_bases_factory.CreateRuleBase(i_name))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'