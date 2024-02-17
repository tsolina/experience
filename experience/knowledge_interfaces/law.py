from experience.knowledge_interfaces import Relation

class Law(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Law
    """

    def __init__(self, com):
        super().__init__(com)
        self.law = com

    def add_formal_parameter(self, i_name: str, i_magnitude: str) -> 'Law':
        return self.law.AddFormalParameter(i_name, i_magnitude)

    def remove_formal_parameter(self, i_name: str) -> 'Law':
        return self.law.RemoveFormalParameter(i_name)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'