from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMOccurrence

if TYPE_CHECKING:
    from experience.inf_interfaces import Position
    from experience.product_structure_client_interfaces import VPMInstance, VPMOccurrences

class VPMOccurrence(PLMOccurrence):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMOccurrence
                |                       VPMOccurrence 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_occurrence = com

    def instance_occurrence_of(self) -> 'VPMInstance':
        from experience.product_structure_client_interfaces import VPMInstance
        return VPMInstance(self.vpm_occurrence.InstanceOccurrenceOf)
    
    def occurrences(self) -> 'VPMOccurrences':
        from experience.product_structure_client_interfaces import VPMOccurrences
        return VPMOccurrences(self.vpm_occurrence.Occurrences)
    
    def position(self) -> 'Position':
        from experience.inf_interfaces import Position
        return Position(self.vpm_occurrence.Position)

    def __repr__(self):
        return f'VPMOccurrence(name="{self.name}")'