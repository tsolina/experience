from typing import Iterator, TYPE_CHECKING

from experience.system import Collection
from .cat_kin_mechanism_types import *
from experience.cat_eng_connection_interfaces.eng_connection import EngConnection

if TYPE_CHECKING:
    from experience.types import cat_variant

class KinJoints(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinJoints
    """

    def __init__(self, com):
        super().__init__(com, child=EngConnection)
        self.kin_joints = com

    def exclude(self, i_index: 'cat_variant') -> 'KinJoints':
        self.kin_joints.Exclude(i_index)
        return self
    
    def include(self, i_joint: EngConnection) -> 'KinJoints':
        self.kin_joints.Include(i_joint._com)
        return self

    def item(self, i_index: 'cat_variant') -> EngConnection:
        return EngConnection(self.kin_joints.Item(i_index))

    def __getitem__(self, n: int) -> EngConnection:
        if (n + 1) > self.count():
            raise StopIteration

        return EngConnection(self.kin_joints.item(n + 1))

    def __iter__(self) -> Iterator[EngConnection]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
