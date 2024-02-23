from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import Pattern

if TYPE_CHECKING:
    from experience.knowledge_interfaces import IntParam
    from experience.cat_part_interfaces import LinearRepartition

class RectPattern(Pattern):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             PartInterfaces.Pattern
                |                                 RectPattern
    """

    def __init__(self, com):
        super().__init__(com)
        self.rect_pattern = com

    def first_direction_repartition(self) -> 'LinearRepartition':
        from experience.cat_part_interfaces import LinearRepartition
        return LinearRepartition(self.rect_pattern.FirstDirectionRepartition)

    def first_direction_row(self) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.rect_pattern.FirstDirectionRow)

    def first_orientation(self, value: bool = None) -> Union['RectPattern', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rect_pattern.FirstOrientation = value
            return self
        return self.rect_pattern.FirstOrientation

    def first_rectangular_pattern_parameters(self, value: CatRectangularPatternParameters = None) -> Union['RectPattern', CatRectangularPatternParameters]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rect_pattern.FirstRectangularPatternParameters = int(value)
            return self
        return CatRectangularPatternParameters.item(self.rect_pattern.FirstRectangularPatternParameters)

    def second_direction_repartition(self) -> 'LinearRepartition':
        from experience.cat_part_interfaces import LinearRepartition
        return LinearRepartition(self.rect_pattern.SecondDirectionRepartition)

    def second_direction_row(self) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.rect_pattern.SecondDirectionRow)

    def second_orientation(self, value: bool = None) -> Union['RectPattern', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rect_pattern.SecondOrientation = value
            return self
        return self.rect_pattern.SecondOrientation

    def second_rectangular_pattern_parameters(self, value: CatRectangularPatternParameters = None) -> Union['RectPattern', CatRectangularPatternParameters]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.rect_pattern.SecondRectangularPatternParameters = int(value)
            return self
        return CatRectangularPatternParameters.item(self.rect_pattern.SecondRectangularPatternParameters)

    def get_first_direction(self, io_first_direction: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetFirstDirection", 2)

    def get_second_direction(self, io_second_direction: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetSecondDirection", 2)

    def set_first_direction(self, i_first_direction: Reference) -> 'RectPattern':
        self.rect_pattern.SetFirstDirection(i_first_direction._com)
        return self

    def set_instance_spacing(self, i_instance_number: int, i_spacing: float, i_direction: int) -> 'RectPattern':
        self.rect_pattern.SetInstanceSpacing(i_instance_number, i_spacing, i_direction)
        return self

    def set_second_direction(self, i_second_direction: Reference) -> 'RectPattern':
        self.rect_pattern.SetSecondDirection(i_second_direction._com)
        return self

    def set_unequal_instance_number(self, i_instance_number: int, i_direction: int) -> 'RectPattern':
        self.rect_pattern.SetUnequalInstanceNumber(i_instance_number, i_direction)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'