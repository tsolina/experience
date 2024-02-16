from experience.knowledge_interfaces import Dimension

class Length(Dimension):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         KnowledgeInterfaces.RealParam
                |                             KnowledgeInterfaces.Dimension
                |                                 Length
    """

    def __init__(self, com):
        super().__init__(com)
        self.length = com

    def __repr__(self):
        return f'Length(name="{ self.name()}")'