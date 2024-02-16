from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMRepInstance

class VPMRepOccurrence(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VPMRepOccurrence 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_rep_occurrence = com

    def related_rep_instance(self) -> 'VPMRepInstance':
        from experience.product_structure_client_interfaces import VPMRepInstance
        return VPMRepInstance(self.vpm_rep_occurrence.RelatedRepInstance)

    def __repr__(self):
        return f'VPMRepOccurrence(name="{self.name()}")'