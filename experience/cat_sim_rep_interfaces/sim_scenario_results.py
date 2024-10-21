from typing import Iterator, TYPE_CHECKING

from experience.cat_sim_rep_interfaces.sim_scenario_result import SimScenarioResult
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class SimScenarioResults(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimScenarioResults
    """

    def __init__(self, com):
        super().__init__(com, child=SimScenarioResult)
        self.sim_scenario_results = com

    def item(self, i_index: 'cat_variant') -> SimScenarioResult:
        return SimScenarioResult(self.sim_scenario_results.Item(i_index))

    def __getitem__(self, n: int) -> SimScenarioResult:
        if (n + 1) > self.count():
            raise StopIteration

        return SimScenarioResult(self.sim_scenario_results.item(n + 1))

    def __iter__(self) -> Iterator[SimScenarioResult]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
