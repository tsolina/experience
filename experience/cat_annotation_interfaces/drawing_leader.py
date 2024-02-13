from typing import TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_annotation_interfaces import DrawingLeaders

class DrawingLeader(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingLeader
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_leader = com

    def all_around(self, value: bool = None) -> Union['DrawingLeader', bool]:
        if value is not None:
            self.drawing_leader.AllAround = value
            return self
        return self.drawing_leader.AllAround

    def anchor_point(self, value: int = None) -> Union['DrawingLeader', int]:
        if value is not None:
            self.drawing_leader.AnchorPoint = value
            return self
        return self.drawing_leader.AnchorPoint

    def anchor_symbol(self, value: int = None) -> Union['DrawingLeader', int]:
        if value is not None:
            self.drawing_leader.AnchorSymbol = value
            return self
        return self.drawing_leader.AnchorSymbol

    def head_symbol(self, value: int = None) -> Union['DrawingLeader', int]:
        if value is not None:
            self.drawing_leader.HeadSymbol = value
            return self
        return self.drawing_leader.HeadSymbol

    def head_target(self, value: AnyObject = None) -> Union['DrawingLeader', AnyObject]:
        if value is not None:
            self.drawing_leader.HeadTarget = value._com
            return self
        return AnyObject(self.drawing_leader.HeadTarget)

    def leaders(self) -> 'DrawingLeaders':
        from experience.cat_annotation_interfaces import DrawingLeaders
        return DrawingLeaders(self.drawing_leader.Leaders)

    def nb_interruption(self) -> int:
        return self.drawing_leader.NbInterruption

    def nb_point(self) -> int:
        return self.drawing_leader.NbPoint

    def add_interruption(self, i_first_point_x: float, i_first_point_y: float, i_second_point_x: float, i_second_point_y: float) -> 'DrawingLeader':
        self.drawing_leader.AddInterruption(i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y)
        return self

    def add_point(self, i_num: int, i_x: float, i_y: float) -> 'DrawingLeader':
        self.drawing_leader.AddPoint(i_num, i_x, i_y)
        return self

    def get_interruptions(self) -> tuple: #, o_interruptions: tuple
        return self.drawing_leader.GetInterruptions()

    def get_point(self, i_num: int) -> tuple[float, float]:
        return self.drawing_leader.GetPoint(i_num)

    def get_points(self) -> tuple: #, o_points: tuple
        return self.drawing_leader.GetPoints()

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> 'DrawingLeader':
        self.drawing_leader.ModifyPoint(i_num, i_x, i_y)
        return self

    def remove_interruption(self, i_num: int) -> 'DrawingLeader':
        self.drawing_leader.RemoveInterruption(i_num)
        return self

    def remove_point(self, i_num: int) -> 'DrawingLeader':
        self.drawing_leader.RemovePoint(i_num)
        return self

    def __repr__(self):
        return f'DrawingLeader(name="{self.name()}")'
