from experience.knowledge_interfaces.knowledge_set import KnowledgeSet

class ExpertRuleBasesSet(KnowledgeSet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeSet
                |                         ExpertRuleBasesSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.expect_rule_bases_set = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'