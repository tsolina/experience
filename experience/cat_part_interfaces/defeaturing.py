from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.dress_up_shape import DressUpShape

if TYPE_CHECKING:
    from experience.cat_part_interfaces import DefeaturingFilters

class Defeaturing(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Defeaturing
    """

    def __init__(self, com):
        super().__init__(com)
        self.defeaturing = com

    def filters(self) -> 'DefeaturingFilters':
        from experience.cat_part_interfaces import DefeaturingFilters
        return DefeaturingFilters(self.defeaturing.Filters)

    def __repr__(self):
        return f'Defeaturing(name="{ self.name() }")'