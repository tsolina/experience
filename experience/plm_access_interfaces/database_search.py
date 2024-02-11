from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.plm_modeler_base_interfaces import PLMEntities


class DatabaseSearch(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatabaseSearch
    """

    def __init__(self, com):
        super().__init__(com)
        self.database_search = com

    def all_minor_versions(self, i_all_minor_versions: int) -> 'DatabaseSearch':
        self.database_search.AllMinorVersions = i_all_minor_versions
        return self
    
    def base_type(self, i_base_type: str) -> 'DatabaseSearch':
        self.database_search.BaseType = i_base_type
        return self
        
    def condition(self, i_condition: int) -> 'DatabaseSearch':
        """
        enum SearchCondition {
            SearchCondition_AND,
            SearchCondition_OR
        } 
        """
        self.database_search.Condition = i_condition
        return self
    
    def extension(self, i_extension: str) -> 'DatabaseSearch':
        self.database_search.Extension = i_extension
        return self   
    
    def latest_version(self, i_latest_version: int) -> 'DatabaseSearch':
        self.database_search.LatestVersion = i_latest_version
        return self

    def mode(self, i_mode: int) -> 'DatabaseSearch':
        """
        enum SearchMode {
        SearchMode_Easy,
        SearchMode_Extended,
        SearchMode_Expert,
        SearchMode_Predefined
        }  
        """
        self.database_search.Mode = i_mode
        return self
    
    def page_count(self) -> int:
        return self.database_search.PageCount 

    def results(self) -> 'PLMEntities':
        from experience.plm_modeler_base_interfaces import PLMEntities
        return PLMEntities(self.database_search.Results)
    
    def search_count(self) -> int:
        return self.database_search.SearchCount

    def title(self, i_title: str) -> 'DatabaseSearch':
        self.database_search.Title = i_title
        return self 
           
    def add_easy_criteria(self, i_attr_id: str, i_attr_value: str) -> 'DatabaseSearch':
        self.database_search.AddEasyCriteria(i_attr_id, i_attr_value)
        return self   
    
    def add_extended_criteria(self, i_attr_id: str, i_attr_value: str, i_operator: int) -> 'DatabaseSearch':
        """ i_operator
        enum SearchOperator {
        SearchOperator_EQ,
        SearchOperator_NOT_EQ,
        SearchOperator_LIKE,
        SearchOperator_NOT_LIKE,
        SearchOperator_LT,
        SearchOperator_LT_EQ,
        SearchOperator_GT,
        SearchOperator_GT_EQ,
        SearchOperator_BETWEEN,
        SearchOperator_NOT_BETWEEN,
        SearchOperator_NULL,
        SearchOperator_NOT_NULL
        } 
        """
        self.database_search.AddExtendedCriteria(i_attr_id, i_attr_value, i_operator)
        return self 
    
    def add_extended_range_criteria(self, i_attr_id: str, i_attr_start_value: str, i_attr_end_value: str, i_operator: int) -> 'DatabaseSearch':
        """ i_operator
        enum SearchOperator {
        SearchOperator_EQ,
        SearchOperator_NOT_EQ,
        SearchOperator_LIKE,
        SearchOperator_NOT_LIKE,
        SearchOperator_LT,
        SearchOperator_LT_EQ,
        SearchOperator_GT,
        SearchOperator_GT_EQ,
        SearchOperator_BETWEEN,
        SearchOperator_NOT_BETWEEN,
        SearchOperator_NULL,
        SearchOperator_NOT_NULL
        } 
        """
        self.database_search.AddExtendedRangeCriteria(i_attr_id, i_attr_start_value, i_attr_end_value, i_operator)
        return self 
    
    def add_predefined_criteria(self, i_criteria_with_pq_abbreviation: str) -> 'DatabaseSearch':
        self.database_search.AddPredefinedCriteria(i_criteria_with_pq_abbreviation)
        return self 
    
    def next_page(self) -> 'DatabaseSearch':
        self.database_search.NextPage()
        return self     

    def set_expert_expression(self, i_expression: str) -> 'DatabaseSearch':
        self.database_search.SetExpertExpression(i_expression)
        return self  

    def sort_by(self, i_sort_by_attr: str, i_sort_order: int) -> 'DatabaseSearch':
        """ i_sort_order
        enum SearchSortOrder {
        SearchSortOrder_Ascending,
        SearchSortOrder_Descending
        } 
        """
        self.database_search.SortBy(i_sort_by_attr, i_sort_order)
        return self        

    def __repr__(self):
        return f'DatabaseSearch(name="{self.name()}")'