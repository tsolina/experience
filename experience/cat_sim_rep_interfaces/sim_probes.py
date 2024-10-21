from typing import Iterator, TYPE_CHECKING

from experience.cat_sim_rep_interfaces.sim_probe import SimProbe
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class SimProbes(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimProbes
    """

    def __init__(self, com):
        super().__init__(com, child=SimProbe)
        self.sim_probes = com

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str) -> SimProbe:
        return SimProbe(self.sim_probes.Add(i_type, i_catalog_name, i_client_id))

    def item(self, i_index: 'cat_variant') -> SimProbe:
        return SimProbe(self.sim_probes.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'SimProbes':
        self.sim_probes.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> SimProbe:
        if (n + 1) > self.count():
            raise StopIteration

        return SimProbe(self.sim_probes.item(n + 1))

    def __iter__(self) -> Iterator[SimProbe]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
