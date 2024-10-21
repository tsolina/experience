from typing import Iterator, TYPE_CHECKING

from experience.cat_behavior_interfaces.dpc_operation import DPCOperation
from experience.system import Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class DPCOperations(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DPCOperations
    """

    def __init__(self, com):
        super().__init__(com, child=DPCOperation)
        self.dpc_operations = com

    def item(self, i_index: 'cat_variant') -> DPCOperation:
        return DPCOperation(self.dpc_operations.Item(i_index))
    
    def operate(self, operation_name: str) -> DPCOperation:
        return DPCOperation(self.dpc_operations.Operate(operation_name))
    
    def __getitem__(self, n: int) -> DPCOperation:
        if (n + 1) > self.count():
            raise StopIteration

        return DPCOperation(self.dpc_operations.item(n + 1))

    def __iter__(self) -> Iterator[DPCOperation]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
