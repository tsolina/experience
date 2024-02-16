from typing import Iterator

from experience.mecmod_interfaces import AxisSystem
from experience.system import Collection
from experience.types import cat_variant


class AxisSystems(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AxisSystems
    """

    def __init__(self, com):
        super().__init__(com, child=AxisSystem)
        self.axis_systems = com

    def add(self) -> AxisSystem:
        return AxisSystem(self.axis_systems.Add())

    def item(self, i_index: cat_variant) -> AxisSystem:
        return AxisSystem(self.axis_systems.Item(i_index))

    def __getitem__(self, n: int) -> AxisSystem:
        if (n + 1) > self.count():
            raise StopIteration

        return AxisSystem(self.axis_systems.item(n + 1))

    def __iter__(self) -> Iterator[AxisSystem]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'AxisSystems(name="{self.name()}")'