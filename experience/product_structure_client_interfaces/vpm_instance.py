from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.inf_interfaces import Position
    from experience.product_structure_client_interfaces import VPMReference

class VPMInstance(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMInstance 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_instance = com

    def position(self) -> 'Position':
        from experience.inf_interfaces import Position
        return Position(self.vpm_instance.Position)

    def reference_instance_of(self) -> 'VPMReference':
        from experience.product_structure_client_interfaces import VPMReference
        return VPMReference(self.vpm_instance.ReferenceInstanceOf)

    def __repr__(self):
        return f'VPMInstance(name="{self.name}")'