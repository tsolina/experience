from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces import IntParam

class Repartition(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Repartition
    """

    def __init__(self, com):
        super().__init__(com)
        self.repartition = com

    def instances_count(self) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.repartition.InstancesCount)

    def __repr__(self):
        return f'Repartition(name="{ self.name }")'