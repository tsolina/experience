from typing import Iterator, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntities
from experience.product_structure_client_interfaces import VPMPublication

if TYPE_CHECKING:
    from experience.types import cat_variant

class VPMPublications(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMPublications
    """

    def __init__(self, com):
        super().__init__(com, child=VPMPublication)
        self.vpm_publications = com

    def __repr__(self):
        return f'VPMPublications(name="{self.name()}")'