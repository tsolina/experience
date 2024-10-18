from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.inf_interfaces import Service
from experience.cat_opns_section_interfaces import Section
from experience.types import cat_variant

# if TYPE_CHECKING:
#     from experience.cat_opns_section_interfaces import Section

class SectionService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SectionService
    """

    def __init__(self, com):
        super().__init__(com)
        self.section_service = com

    def add(self) -> 'Section':
        return Section(self.section_service.Add())

    def count(self) -> int:
        return self.section_service.Count()
    
    def item(self, i_index: 'cat_variant') -> Section:
        return Section(self.section_service.Item(i_index))
    
    def remove(self, i_index: 'cat_variant') -> 'SectionService':
        self.section_service.Remove(i_index)
        return self
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'