from typing import Iterator, TYPE_CHECKING

from experience.cat_sim_rep_interfaces.sim_excitation import SimExcitation
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class SimExcitations(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimExcitations
    """

    def __init__(self, com):
        super().__init__(com, child=SimExcitation)
        self.sim_excitations = com

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str) -> SimExcitation:
        return SimExcitation(self.sim_excitations.Add(i_type, i_catalog_name, i_client_id))

    def item(self, i_index: 'cat_variant') -> SimExcitation:
        return SimExcitation(self.sim_excitations.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'SimExcitations':
        self.sim_excitations.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> SimExcitation:
        if (n + 1) > self.count():
            raise StopIteration

        return SimExcitation(self.sim_excitations.item(n + 1))

    def __iter__(self) -> Iterator[SimExcitation]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
