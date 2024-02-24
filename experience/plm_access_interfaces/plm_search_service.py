from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.plm_access_interfaces import PLMSearches

class PLMSearchService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMApplicationContextIDLItf.PLMAppContext
                |                             PLMSearchService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_search_service = com

    def searches(self) -> 'PLMSearches':
        from experience.plm_access_interfaces import PLMSearches
        return PLMSearches(self.plm_search_service.Searches)