from typing import Union, Optional, TYPE_CHECKING

#from experience.system import AnyObject
from experience.plm_modeler_base_interfaces import PLMOccurrence

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMOccurrences, VPMReference, VPMRepOccurrences

class VPMRootOccurrence(PLMOccurrence):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMOccurrence
                |                       VPMRootOccurrence
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_root_occurrence = com

    def occurrences(self) -> 'VPMOccurrences':
        from experience.product_structure_client_interfaces import VPMOccurrences
        return VPMOccurrences(self.vpm_root_occurrence.Occurrences)

    def reference_root_occurrence_of(self) -> 'VPMReference':
        from experience.product_structure_client_interfaces import VPMReference
        return VPMReference(self.vpm_root_occurrence.ReferenceRootOccurrenceOf)
    
    def rep_occurrences(self) -> 'VPMRepOccurrences':
        from experience.product_structure_client_interfaces import VPMRepOccurrences
        return VPMRepOccurrences(self.vpm_root_occurrence.RepOccurrences)

    def __repr__(self):
        return f'VPMRootOccurrence(name="{self.name()}")'