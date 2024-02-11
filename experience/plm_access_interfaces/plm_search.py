from typing import Union, Optional, TYPE_CHECKING

from experience.plm_application_context_interfaces import PLMAppContext

if TYPE_CHECKING:
    from experience.inf_interfaces import Editor
    from experience.plm_access_interfaces import PLMSearches

class PLMSearch(PLMAppContext):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMApplicationContextIDLItf.PLMAppContext
                |                             PLMSearch
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_search = com
    
    def editor(self) -> 'Editor':
        from experience.inf_interfaces import Editor
        return Editor(self.plm_search.Editor)

    def type(self, i_type_bstr: str) -> 'PLMSearch':
        self.plm_search.Type = i_type_bstr
        return self
    
    def add_attribute_criteria(self, i_attr_id_bstr: str, i_attr_value_bstr: str) -> 'PLMSearch':
        self.plm_search.AddAttributeCriteria(i_attr_id_bstr, i_attr_value_bstr)
        return self
    
    def search(self) -> 'PLMSearch':
        self.plm_search.Search()
        return self
    
    def searches(self) -> 'PLMSearches':
        from experience.plm_access_interfaces import PLMSearches
        return PLMSearches(self.plm_search.Searches)

    def __repr__(self):
        return f'PLMSearch(name="{self.name()}")'