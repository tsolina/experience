from typing import Union
from experience.system import AnyObject
from experience.cat_annotation_interfaces.annotation_types import *

class DrawingArrow(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingArrow
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_arrow = com

    def head_symbol(self, value: CatSymbolType = None) -> Union['DrawingArrow', CatSymbolType]:
        if value is not None:
            self.drawing_arrow.HeadSymbol = int(value)
            return self
        return CatSymbolType.item(self.drawing_arrow.HeadSymbol)

    def head_target(self, value: AnyObject = None) -> Union['DrawingArrow', AnyObject]:
        if value is not None:
            self.drawing_arrow.HeadTarget = value
            return self
        return AnyObject(self.drawing_arrow.HeadTarget)

    def nb_interruption(self) -> int:
        return self.drawing_arrow.NbInterruption

    def nb_point(self) -> int:
        return self.drawing_arrow.NbPoint

    def tail_symbol(self, value: CatSymbolType = None) -> Union['DrawingArrow', CatSymbolType]:
        if value is not None:
            self.drawing_arrow.TailSymbol = int(value)
            return self
        return CatSymbolType.item(self.drawing_arrow.TailSymbol)

    def tail_target(self, value: AnyObject = None) -> Union['DrawingArrow', AnyObject]:
        if value is not None:
            self.drawing_arrow.TailTarget = value
            return self
        return AnyObject(self.drawing_arrow.TailTarget)

    def add_interruption(self, i_first_point_x: float, i_first_point_y: float, i_second_point_x: float, i_second_point_y: float) -> 'DrawingArrow':
        self.drawing_arrow.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)
        return self

    def add_point(self, i_num: int, i_x: float, i_y: float) -> 'DrawingArrow':
        self.drawing_arrow.AddPoint(i_num, i_x, i_y)
        return self

    def get_interruptions(self) -> tuple:
        if self.nb_interruption() == 0:
            return ()
        return self._get_safe_array(self.drawing_arrow, "GetInterruptions", self.nb_interruption() * 2 - 1)

    def get_point(self, i_num: int) -> tuple[float, float]:
        return self.drawing_arrow.GetPoint(i_num)

    def get_points(self) -> tuple:
        if self.nb_point() == 0:
            return ()
        return self._get_safe_array(self.drawing_arrow, "GetPoints", self.nb_point() * 2 - 1)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> 'DrawingArrow':
        self.drawing_arrow.ModifyPoint(i_num, i_x, i_y)
        return self

    def remove_interruption(self, i_num: int) -> 'DrawingArrow':
        self.drawing_arrow.RemoveInterruption(i_num)
        return self

    def remove_point(self, i_num: int) -> 'DrawingArrow':
        self.drawing_arrow.RemovePoint(i_num)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
