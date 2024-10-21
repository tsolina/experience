from experience.system import AnyObject

class SimGenerativeSpecification(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGenerativeSpecification
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_generative_specification = com
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'