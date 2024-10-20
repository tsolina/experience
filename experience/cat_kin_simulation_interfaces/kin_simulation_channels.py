from typing import Iterator, TYPE_CHECKING

from experience.cat_kin_simulation_interfaces.kin_simulation_channel import KinSimulationChannel
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class KinSimulationChannels(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinSimulationChannels
    """

    def __init__(self, com):
        super().__init__(com, child=KinSimulationChannel)
        self.kin_simulation_channels = com

    def item(self, i_index: 'cat_variant') -> KinSimulationChannel:
        return KinSimulationChannel(self.kin_simulation_channels.Item(i_index))

    def __getitem__(self, n: int) -> KinSimulationChannel:
        if (n + 1) > self.count():
            raise StopIteration

        return KinSimulationChannel(self.kin_simulation_channels.item(n + 1))

    def __iter__(self) -> Iterator[KinSimulationChannel]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
