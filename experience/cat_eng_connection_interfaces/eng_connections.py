from typing import Iterator, TYPE_CHECKING

from .cat_eng_connection_types import *
from experience.cat_eng_connection_interfaces.eng_connection import EngConnection
from experience.system import AnyObject, Collection

if TYPE_CHECKING:
    from experience.types import cat_variant

class EngConnections(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     EngConnections
    """

    def __init__(self, com):
        super().__init__(com, child=EngConnection)
        self.eng_connections = com

    def add(self, i_type: CatEngConnectionType, i_impacteds: list) -> EngConnection:
        return EngConnection(self.eng_connections.Add(int(i_type), i_impacteds))
    
    def add_with_context(self, i_type: CatEngConnectionType, i_impacteds: list, i_reference_context: AnyObject, i_name_bstr: str) -> EngConnection:
        return EngConnection(int(i_type, i_impacteds, i_reference_context._com, i_name_bstr))

    def item(self, i_index: 'cat_variant') -> EngConnection:
        return EngConnection(self.eng_connections.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> 'EngConnections':
        self.eng_connections.Remove(i_index)
        return self

    def __getitem__(self, n: int) -> EngConnection:
        if (n + 1) > self.count():
            raise StopIteration

        return EngConnection(self.eng_connections.item(n + 1))

    def __iter__(self) -> Iterator[EngConnection]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
