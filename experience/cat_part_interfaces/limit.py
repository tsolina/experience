from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.system import AnyObject
from experience.cat_part_interfaces.cat_part_types import *

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class Limit(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Limit
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.limit = com_object

    def dimension(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.limit.Dimension)

    def limit_mode(self, value: CatLimitMode = None) -> Union['Limit', CatLimitMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.limit.LimitMode = int(value)
            return self
        return CatLimitMode.item(self.limit.LimitMode)

    def limiting_element(self, value: Reference = None) -> Union['Limit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.limit.LimitingElement = value._com
            return self
        return Reference(self.limit.LimitingElement)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'