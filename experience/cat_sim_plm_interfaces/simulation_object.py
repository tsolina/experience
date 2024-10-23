
from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

class SimulationObject(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         SimulationObject
    """

    def __init__(self, com):
        super().__init__(com)
        self.simulation_object = com
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'