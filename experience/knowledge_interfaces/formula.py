from experience.knowledge_interfaces import Relation

class Formula(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Formula
    """

    def __init__(self, com):
        super().__init__(com)
        self.formula = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'