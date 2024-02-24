from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntity

class PLMRefreshService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMRefreshService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_refresh_service = com

    def add_object_to_refresh(self, i_plm_entity: 'PLMEntity') -> 'PLMRefreshService':
        self.plm_refresh_service.AddObjectToRefresh(i_plm_entity._com)
        return self
    
    def perform_refresh(self) -> 'PLMRefreshService':
        self.plm_refresh_service.PerformRefresh()
        return self

    def get_concurrent_engineering_status(self) -> tuple:
        return self._get_multi([self.plm_refresh_service], ("AnyObject", "getConcurrentEngineeringStatus"), ["()Variant"])