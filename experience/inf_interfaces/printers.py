from typing import Iterator

from experience.inf_interfaces.printer import Printer
from experience.system.collection import Collection
from experience.types.general import cat_variant

class Printers(Collection):
    def __init__(self, com):
        super().__init__(com, _child=Printer)
        self.printers = com

    def item(self, i_index: cat_variant) -> Printer:
        return Printer(self.printers.Item(i_index))

    def __getitem__(self, n: int) -> Printer:
        if (n + 1) > self.count:
            raise StopIteration

        return Printer(self.printers.item(n + 1))

    def __iter__(self) -> Iterator[Printer]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Printers(name="{self.name}")'
