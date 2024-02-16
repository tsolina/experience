from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntities


class IndexedSearch(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     IndexedSearch
    """

    def __init__(self, com):
        super().__init__(com)
        self.indexed_search = com

    def extension(self, i_externsion: str) -> 'IndexedSearch':
        self.indexed_search.Extensions = i_externsion
        return self
    
    def max_search_result_count(self, i_max_result_count: int) -> 'IndexedSearch':
        """ 200 is maximum """
        self.indexed_search.MaxSearchResultCount = i_max_result_count
        return self   

    def results(self) -> 'PLMEntities':
        from experience.plm_modeler_base_interfaces import PLMEntities
        return PLMEntities(self.indexed_search.Results)
    
    def search_count(self) -> int:
        return self.indexed_search.SearchCount

    def types(self, i_base_type: str) -> 'IndexedSearch':
        self.indexed_search.Types = i_base_type
        return self
    
    def predicate(self, i_predicate: str, i_value: str) -> 'IndexedSearch':
        self.indexed_search.Predicate(i_predicate, i_value)
        return self    
    
    def search(self) -> 'IndexedSearch':
        self.indexed_search.Search()
        return self       
    
    def sort_by(self, i_sort_by_predicate: str, i_sort_order: int) -> 'IndexedSearch':
        """ i_sort_order:
        enum SearchSortOrder {
        SearchSortOrder_Ascending,
        SearchSortOrder_Descending
        }  
        """
        self.indexed_search.SortBy(i_sort_by_predicate, i_sort_order)
        return self     

    def __repr__(self):
        return f'IndexedSearch(name="{self.name()}")'