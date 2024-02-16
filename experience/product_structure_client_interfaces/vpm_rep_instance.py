from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMRepReference, Shape3D

class VPMRepInstance(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMRepInstance 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_rep_instance = com

    def reference_instance_of(self) -> 'VPMRepReference':
        from experience.product_structure_client_interfaces import VPMRepReference
        return VPMRepReference(self.vpm_rep_instance.ReferenceInstanceOf)

    def __repr__(self):
        return f'VPMRepInstance(name="{self.name()}")'