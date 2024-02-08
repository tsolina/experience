from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import TransformationShape
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces.angle import Angle

class Pattern(TransformationShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             Pattern
    """

    def __init__(self, com):
        super().__init__(com)
        self.pattern = com

    def item_to_copy(self, value: AnyObject = None) -> Union['Pattern', AnyObject]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.pattern.ItemToCopy = value._com
            return self
        return AnyObject(self.pattern.ItemToCopy)

    def rotation_angle(self) -> 'Angle':
        from experience.knowledge_interfaces.angle import Angle
        return Angle(self.pattern.RotationAngle)

    def activate_position(self, i_pos_u: int, i_pos_v: int) -> 'Pattern':
        self.pattern.ActivatePosition(i_pos_u, i_pos_v)
        return self

    def desactivate_position(self, i_pos_u: int, i_pos_v: int) -> 'Pattern':
        self.pattern.DesactivatePosition(i_pos_u, i_pos_v)
        return self

    def __repr__(self):
        return f'Pattern(name="{ self.name }")'