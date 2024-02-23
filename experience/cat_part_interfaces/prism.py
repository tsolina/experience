from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import SketchBasedShape

if TYPE_CHECKING:
    from experience.cat_part_interfaces import Limit

class Prism(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Prism
    """

    def __init__(self, com):
        super().__init__(com)
        self.prism = com

    def direction_orientation(self, value: CatPrismOrientation = None) -> Union['Prism', CatPrismOrientation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.DirectionOrientation = int(value)
            return self
        return CatPrismOrientation.item(self.prism.DirectionOrientation)

    def direction_type(self, value: CatPrismExtrusionDirection = None) -> Union['Prism', CatPrismExtrusionDirection]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.DirectionType = int(value)
            return self
        return CatPrismExtrusionDirection.item(self.prism.DirectionType)

    def first_limit(self) -> 'Limit':
        from experience.cat_part_interfaces import Limit
        return Limit(self.prism.FirstLimit)

    def is_symmetric(self, value: bool = None) -> Union['Prism', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.IsSymmetric = value
            return self
        return self.prism.IsSymmetric

    def is_thin(self, value: bool = None) -> Union['Prism', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.IsThin = value
            return self
        return self.prism.IsThin

    def merge_end(self, value: bool = None) -> Union['Prism', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.MergeEnd = value
            return self
        return self.prism.MergeEnd

    def neutral_fiber(self, value: bool = None) -> Union['Prism', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.prism.NeutralFiber = value
            return self
        return self.prism.NeutralFiber

    def second_limit(self) -> 'Limit':
        from experience.cat_part_interfaces import Limit
        return Limit(self.prism.SecondLimit)

    def get_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetDirection", 2)

    def get_profile_element(self) -> Reference:
        return self.prism.GetProfileElement()

    def reverse_inner_side(self) -> 'Prism':
        self.prism.ReverseInnerSide()
        return self

    def set_direction(self, i_line: Reference) -> 'Prism':
        self.prism.SetDirection(i_line._com)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'