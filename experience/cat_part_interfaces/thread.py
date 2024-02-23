from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import StrParam

class Thread(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Thread
    """

    def __init__(self, com):
        super().__init__(com)
        self.thread = com

    def depth(self, value: float = None) -> Union['Thread', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.Depth = value
            return self
        return self.thread.Depth

    def diameter(self, value: float = None) -> Union['Thread', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.Diameter = value
            return self
        return self.thread.Diameter

    def lateral_face_element(self, value: Reference = None) -> Union['Thread', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.LateralFaceElement = value._com
            return self
        return Reference(self.thread.LateralFaceElement)

    def limit_face_element(self, value: Reference = None) -> Union['Thread', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.LimitFaceElement = value._com
            return self
        return Reference(self.thread.LimitFaceElement)

    def pitch(self, value: float = None) -> Union['Thread', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.Pitch = value
            return self
        return self.thread.Pitch

    def side(self, value: CatThreadSide = None) -> Union['Thread', CatThreadSide]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.thread.Side = int(value)
            return self
        return CatThreadSide.item(self.thread.Side)

    def thread_description(self) -> 'StrParam':
        from experience.knowledge_interfaces import StrParam
        return StrParam(self.thread.ThreadDescription)

    def create_standard_thread_design_table(self, i_standard_type: CatThreadStandard) -> 'Thread':
        self.thread.CreateStandardThreadDesignTable(int(i_standard_type))
        return self

    def create_user_standard_design_table(self, i_standard_name: str, i_path: str) -> 'Thread':
        self.thread.CreateUserStandardDesignTable(i_standard_name, i_path)
        return self

    def reverse_direction(self) -> 'Thread':
        self.thread.ReverseDirection()
        return self

    def set_explicit_polarity(self, i_thread_polarity: CatThreadPolarity) -> 'Thread':
        self.thread.SetExplicitPolarity(int(i_thread_polarity))
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'