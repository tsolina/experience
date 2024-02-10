from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMReference, ParentVPMRepInstances 
    from experience.mecmod_interfaces import Part

class VPMRepReference(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMRepReference 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_rep_reference = com

    def father(self) -> 'VPMReference':
        from experience.product_structure_client_interfaces import VPMReference
        return VPMReference(self.vpm_rep_reference.Father)

    def parent_rep_instances(self) -> 'ParentVPMRepInstances':
        from experience.product_structure_client_interfaces import ParentVPMRepInstances
        return VPMReference(self.vpm_root_occurrence.ParentRepInstances)
    
    def part(self) -> 'Part':
        from experience.mecmod_interfaces import Part
        return Part(self.vpm_rep_reference.getItem("Part"))

    def __repr__(self):
        return f'VPMRepReference(name="{self.name}")'