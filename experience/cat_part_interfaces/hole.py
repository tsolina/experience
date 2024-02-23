from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import SketchBasedShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length, StrParam
    from experience.cat_part_interfaces import Limit

class Hole(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Hole
    """

    def __init__(self, com):
        super().__init__(com)
        self.hole = com

    def anchor_mode(self, value: CatHoleAnchorMode = None) -> Union['Hole', CatHoleAnchorMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.AnchorMode = int(value)
            return self
        return CatHoleAnchorMode.item(self.hole.AnchorMode)

    def bottom_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hole.BottomAngle)

    def bottom_limit(self) -> 'Limit':
        from experience.cat_part_interfaces import Limit
        return Limit(self.hole.BottomLimit)

    def bottom_type(self, value: CatHoleBottomType = None) -> Union['Hole', CatHoleBottomType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.BottomType = int(value)
            return self
        return CatHoleBottomType.item(self.hole.BottomType)

    def counter_drilled_mode(self, value: CatCDHoleMode = None) -> Union['Hole', CatCDHoleMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.CounterDrilledMode = int(value)
            return self
        return CatCDHoleMode.item(self.hole.CounterDrilledMode)

    def counter_sunk_mode(self, value: CatCSHoleMode = None) -> Union['Hole', CatCSHoleMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.CounterSunkMode = int(value)
            return self
        return CatCSHoleMode.item(self.hole.CounterSunkMode)

    def diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.Diameter)

    def head_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hole.HeadAngle)

    def head_depth(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.HeadDepth)

    def head_diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.HeadDiameter)

    def hole_thread_description(self) -> 'StrParam':
        from experience.knowledge_interfaces import StrParam
        return StrParam(self.hole.HoleThreadDescription)

    def thread_depth(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.ThreadDepth)

    def thread_diameter(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.ThreadDiameter)

    def thread_pitch(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hole.ThreadPitch)

    def thread_side(self, value: CatHoleThreadSide = None) -> Union['Hole', CatHoleThreadSide]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.ThreadSide = int(value)
            return self
        return CatHoleThreadSide.item(self.hole.ThreadSide)

    def threading_mode(self, value: CatHoleThreadingMode = None) -> Union['Hole', CatHoleThreadingMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.ThreadingMode = int(value)
            return self
        return CatHoleThreadingMode.item(self.hole.ThreadingMode)

    def type(self, value: CatHoleType = None) -> Union['Hole', CatHoleType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hole.Type = int(value)
            return self
        return CatHoleType.item(self.hole.Type)

    def create_standard_thread_design_table(self, i_standard_type: CatHoleThreadStandard) -> 'Hole':
        self.hole.CreateStandardThreadDesignTable(int(i_standard_type))
        return self

    def create_user_standard_design_table(self, i_standard_name: str, i_path: str) -> 'Hole':
        self.hole.CreateUserStandardDesignTable(i_standard_name, i_path)
        return self

    def get_direction(self) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetDirection", 2)

    def get_origin(self, io_origin: tuple) -> None:
        return self._get_safe_array(self._com, "GetOrigin", 2)

    def reverse(self) -> 'Hole':
        self.hole.Reverse()
        return self

    def set_direction(self, i_direction: Reference) -> 'Hole':
        self.hole.SetDirection(i_direction._com)
        return self

    def set_origin(self, i_x: float, i_y: float, i_z: float) -> 'Hole':
        self.hole.SetOrigin(i_x, i_y, i_z)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'