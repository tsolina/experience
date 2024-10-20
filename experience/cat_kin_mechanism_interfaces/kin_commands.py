from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from .cat_kin_mechanism_types import *
from experience.cat_kin_mechanism_interfaces.kin_command import KinCommand

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.cat_eng_connection_interfaces.eng_connection import EngConnection

class KinCommands(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinCommands
    """

    def __init__(self, com):
        super().__init__(com, child=KinCommand)
        self.kin_commands = com

    def add(self, i_joint: 'EngConnection', i_type: CATKinMechanismCommandType) -> KinCommand:
        return KinCommand(self.kin_commands.Add(i_joint._com, int(i_type)))

    def item(self, i_index: 'cat_variant') -> KinCommand:
        return KinCommand(self.kin_commands.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'KinCommands':
        self.kin_commands.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> KinCommand:
        if (n + 1) > self.count():
            raise StopIteration

        return KinCommand(self.kin_commands.item(n + 1))

    def __iter__(self) -> Iterator[KinCommand]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
