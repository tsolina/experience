from typing import Union
from experience.system import AnyObject

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

    def head_symbol(self, value: int = None) -> Union['DrawingArrow', int]:
        if value is not None:
            self.drawing_arrow.HeadSymbol = value
            return self
        return self.drawing_arrow.HeadSymbol

    def head_target(self, value: AnyObject = None) -> Union['DrawingArrow', AnyObject]:
        if value is not None:
            self.drawing_arrow.HeadTarget = value
            return self
        return AnyObject(self.drawing_arrow.HeadTarget)

    def nb_interruption(self) -> int:
        return self.drawing_arrow.NbInterruption

    def nb_point(self) -> int:
        return self.drawing_arrow.NbPoint

    def tail_symbol(self, value: int = None) -> Union['DrawingArrow', int]:
        if value is not None:
            self.drawing_arrow.TailSymbol = value
            return self
        return self.drawing_arrow.TailSymbol

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

    def get_interruptions(self, o_interruptions: tuple) -> tuple:
        return self.drawing_arrow.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> tuple:
        return self.drawing_arrow.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points: tuple) -> tuple:
        return self.drawing_arrow.GetPoints(o_points)

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
        return f'DrawingArrow(name="{self.name()}")'
