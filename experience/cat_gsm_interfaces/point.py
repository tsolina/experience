from typing import Union, Optional, TYPE_CHECKING

from experience.mecmod_interfaces import HybridShape

class Point(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         Point
    """

    def __init__(self, com):
        super().__init__(com)
        self.point_ = com

    def get_coordinates(self) -> tuple:
        return self._get_safe_array(self._com, "GetCoordinates", 2)

    def set_coordinates(self, o_coordinates: tuple) -> 'Point':
        self.point_.SetCoordinates(o_coordinates)
        return self

    def __repr__(self):
        return f'Point(name="{self.name}")'