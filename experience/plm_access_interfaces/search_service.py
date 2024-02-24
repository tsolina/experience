from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.plm_access_interfaces import DatabaseSearch, IndexedSearch

class SearchService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SearchService
    """

    def __init__(self, com):
        super().__init__(com)
        self.search_service = com
    
    def database_search(self) -> 'DatabaseSearch':
        from experience.plm_access_interfaces import DatabaseSearch
        return DatabaseSearch(self.search_service.DatabaseSearch)
    
    def indexed_search(self) -> 'IndexedSearch':
        from experience.plm_access_interfaces import IndexedSearch
        return IndexedSearch(self.search_service.GetItem('IndexedSearch'))
    
    def title(self, i_title: str) -> 'SearchService':
        self.search_service.Title = i_title
        return self
    
    def search(self) -> 'SearchService':
        self.search_service.Search()
        return self