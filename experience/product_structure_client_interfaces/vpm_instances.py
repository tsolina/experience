from typing import Iterator, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntities
from experience.product_structure_client_interfaces import VPMInstance

if TYPE_CHECKING:
    from experience.types import cat_variant

class VPMInstances(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMModelerBaseIDLItf.PLMEntities
                |                          VPMInstances
    """

    def __init__(self, com):
        super().__init__(com, child=VPMInstance)
        self.vpm_publications = com

    def __repr__(self):
        return f'VPMInstances(name="{self.name}")'