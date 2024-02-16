from typing import Iterator, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntities
from experience.product_structure_client_interfaces import VPMRepInstance

if TYPE_CHECKING:
    from experience.types import cat_variant

class VPMRepInstances(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMRepInstances
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_rep_instances = com
        self._child = VPMRepInstance

    def item(self, i_index: 'cat_variant') -> VPMRepInstance:
        return VPMRepInstance(self.vpm_rep_instances.Item(i_index))

    def __getitem__(self, n: int) -> VPMRepInstance:
        if (n + 1) > self.count:
            raise StopIteration
        return VPMRepInstance(self.vpm_rep_instances.item(n + 1))

    def __iter__(self) -> Iterator[VPMRepInstance]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'VPMRepInstances(name="{self.name()}")'