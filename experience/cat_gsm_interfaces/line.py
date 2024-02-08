from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class Line(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         Line
    """

    def __init__(self, com):
        super().__init__(com)
        self.line = com

    def first_upto_elem(self, value: Reference = None) -> Union['Line', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.line.FirstUptoElem = value._com
            return self
        return Reference(self.line.FirstUptoElem)

    def second_upto_elem(self, value: Reference = None) -> Union['Line', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.line.SecondUptoElem = value._com
            return self
        return Reference(self.line.SecondUptoElem)

    def get_direction(self) -> tuple:
        return self._get_safe_array(self._com, "GetDirection", 2)

    def get_origin(self) -> tuple:
        return self._get_safe_array(self._com, "GetOrigin", 2)

    def put_direction(self, i_direction: tuple[float, float, float]) -> 'Line':
        self.line.PutDirection(i_direction)
        return self


    def __repr__(self):
        return f'Line(name="{self.name}")'