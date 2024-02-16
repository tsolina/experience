from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import SketchBasedShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle

class Revolution(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Revolution
    """

    def __init__(self, com):
        super().__init__(com)
        self.revolution = com

    def first_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.revolution.FirstAngle)

    def is_thin(self, value: bool = None) -> Union['Revolution', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.revolution.IsThin = value
            return self
        return self.revolution.IsThin

    def merge_end(self, value: bool = None) -> Union['Revolution', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.revolution.MergeEnd = value
            return self
        return self.revolution.MergeEnd

    def neutral_fiber(self, value: bool = None) -> Union['Revolution', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.revolution.NeutralFiber = value
            return self
        return self.revolution.NeutralFiber

    def revolute_axis(self, value: Reference = None) -> Union['Revolution', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.revolution.RevoluteAxis = value._com
            return self
        return Reference(self.revolution.RevoluteAxis)

    def second_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.revolution.SecondAngle)

    def __repr__(self):
        return f'Revolution(name="{self.name()}")'