from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.system import AnyObject

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

    def limit_mode(self, value: int = None) -> Union['Limit', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.limit.LimitMode = value
            return self
        return self.limit.LimitMode

    def limiting_element(self, value: Reference = None) -> Union['Limit', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.limit.LimitingElement = value._com
            return self
        return Reference(self.limit.LimitingElement)

    def __repr__(self):
        return f'Limit(name="{self.name}")'