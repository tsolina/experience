from experience.inf_interfaces import Service

class PLMPropagateService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMPropagateService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_propagate_service = com
    
    def plm_propagate(self) -> 'PLMPropagateService':
        self.plm_propagate_service.PLMPropagate()   
        return self 

    def save(self) -> 'PLMPropagateService':
        """ - Deprecated - """
        self.plm_propagate_service.Save()   
        return self 
    
    def get_last_error(self) -> tuple[str, int]:
        return self._get_multi([self._com],("PLMPropagateService", "getLastError"),("String", "Long"))