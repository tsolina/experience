from typing import Iterator, TYPE_CHECKING

from experience.cat_sim_rep_interfaces.sim_scenario_spec import SimScenarioSpec
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class SimScenarioSpecs(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimScenarioSpecs
    """

    def __init__(self, com):
        super().__init__(com, child=SimScenarioSpec)
        self.sim_scenario_specs = com

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str, i_behavior_list: list) -> SimScenarioSpec:
        '''
        unclear what are behaviors, if they should be wrapped or not
        '''
        return SimScenarioSpec(self.sim_scenario_specs.Add(i_type, i_catalog_name, i_client_id, i_behavior_list))

    def item(self, i_index: 'cat_variant') -> SimScenarioSpec:
        return SimScenarioSpec(self.sim_scenario_specs.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'SimScenarioSpecs':
        self.sim_scenario_specs.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> SimScenarioSpec:
        if (n + 1) > self.count():
            raise StopIteration

        return SimScenarioSpec(self.sim_scenario_specs.item(n + 1))

    def __iter__(self) -> Iterator[SimScenarioSpec]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
