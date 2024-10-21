from experience.inf_interfaces.service import Service

class ElecImportFinalizerService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         ElecImportFinalizerService
    """

    def __init__(self, com):
        super().__init__(com)
        self.elec_import_finalizer_service = com

    def finalize(self) -> 'ElecImportFinalizerService':
        return ElecImportFinalizerService(self.elec_import_finalizer_service.Finalize())
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'