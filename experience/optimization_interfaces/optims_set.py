from experience.knowledge_interfaces.knowledge_set import KnowledgeSet

class OptimsSet(KnowledgeSet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeSet
                |                         OptimsSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.optims_set = com
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'