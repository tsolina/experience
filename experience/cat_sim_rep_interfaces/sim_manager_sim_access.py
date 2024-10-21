from experience.system import AnyObject

class SimManagerSIMAccess(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimManagerSIMAccess
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_manager_sim_access = com

    def manifest_path(self) -> str:
        return self.sim_manager_sim_access.ManifestPath
    
    def notify_manifest_modification(self) -> 'SimManagerSIMAccess':
        self.sim_manager_sim_access.NotifyManifestModification()
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'