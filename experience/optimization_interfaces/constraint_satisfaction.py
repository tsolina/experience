from experience.knowledge_interfaces.set_of_equation import SetOfEquation

class ConstraintSatisfaction(SetOfEquation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 KnowledgeIDLItf.SetOfEquation
                |                                     ConstraintSatisfaction
    """

    def __init__(self, com):
        super().__init__(com)
        self.constraint_satisfaction = com

    def solve(self) -> 'ConstraintSatisfaction':
        return self.constraint_satisfaction.Solve()
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'