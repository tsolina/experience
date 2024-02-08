from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.cat_part_interfaces import DraftDomains

class Draft(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Draft
    """

    def __init__(self, com):
        super().__init__(com)
        self.draft = com

    def draft_domains(self) -> 'DraftDomains':
        from experience.cat_part_interfaces import DraftDomains
        return DraftDomains(self.draft.DraftDomains)

    def mode(self, value: int = None) -> Union['DraftDomains', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft.Mode = value
            return self
        return self.draft.Mode

    def parting_element(self, value: Reference = None) -> Union['DraftDomains', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft.PartingElement = value._com
            return self
        return Reference(self.draft.PartingElement)

    def __repr__(self):
        return f'Draft(name="{self.name}")'