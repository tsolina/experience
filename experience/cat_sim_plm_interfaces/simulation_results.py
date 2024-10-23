from typing import Iterator, TYPE_CHECKING

from experience.cat_sim_plm_interfaces.simulation_object import SimulationObject
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class SimulationResults(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimulationResults
    """

    def __init__(self, com):
        super().__init__(com, child=SimulationObject)
        self.simulation_results = com

    def item(self, i_index: 'cat_variant') -> SimulationObject:
        return SimulationObject(self.simulation_results.Item(i_index))

    def __getitem__(self, n: int) -> SimulationObject:
        if (n + 1) > self.count():
            raise StopIteration

        return SimulationObject(self.simulation_results.item(n + 1))

    def __iter__(self) -> Iterator[SimulationObject]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
