from experience.knowledge_interfaces import Dimension

class Angle(Dimension):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         KnowledgeInterfaces.RealParam
                |                             KnowledgeInterfaces.Dimension
                |                                 Angle
    """

    def __init__(self, com):
        super().__init__(com)
        self.angle = com

    def __repr__(self):
        return f'Angle(name="{ self.name()}")'