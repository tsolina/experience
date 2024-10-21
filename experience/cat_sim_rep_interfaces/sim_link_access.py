from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class SimLinkAccess(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLinkAccess
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_link_access = com

    def add_link(self, i_name: str, i_link: AnyObject) -> 'SimLinkAccess':
        self.sim_link_access.AddLink(i_name, i_link._com)
        return self
    
    def add_link_with_context(self, i_attr_name: str, i_link: AnyObject, i_context: 'VPMOccurrence') -> 'SimLinkAccess':
        self.sim_link_access.AddLinkWithContext(i_attr_name, i_link._com, i_context._com)
        return self
    
    def get_all_links(self, i_name: str) -> list:
        return self.sim_link_access.GetAllLinks(i_name)
    
    def get_nb_links(self, i_name: str) -> int:
        return self.sim_link_access.GetNbLinks(i_name)
    
    def remove_all_links(self, i_name: str) -> 'SimLinkAccess':
        self.sim_link_access.RemoveAllLinks(i_name)
        return self
    
    def remove_link(self, i_name: str, i_link: AnyObject) -> 'SimLinkAccess':
        self.sim_link_access.RemoveLink(i_name, i_link._com)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'