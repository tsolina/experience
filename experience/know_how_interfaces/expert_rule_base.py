from experience.know_how_interfaces.expert_rule_base_runtime import ExpertRuleBaseRuntime

class ExpertRuleBase(ExpertRuleBaseRuntime):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 KnowHowIDLItf.ExpertRuleBaseRuntime
                |                                     ExpertRuleBase
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_rule_base = com

    def volatile_copy(self) -> ExpertRuleBaseRuntime:
        return ExpertRuleBaseRuntime(self.expert_rule_base.VolatileCopy())

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'