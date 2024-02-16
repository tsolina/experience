from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.repartition import Repartition

if TYPE_CHECKING:
    from experience.knowledge_interfaces.length import Length

class LinearRepartition(Repartition):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartInterfaces.Repartition
                |                         LinearRepartition
    """

    def __init__(self, com):
        super().__init__(com)
        self.linear_repartition = com

    def spacing(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.linear_repartition.Spacing)

    def __repr__(self):
        return f'LinearRepartition(name="{ self.name() }")'