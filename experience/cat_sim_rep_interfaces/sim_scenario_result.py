from experience.system import AnyObject

class SimScenarioResult(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimScenarioResult
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_scenario_result = com
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'