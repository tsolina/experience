from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import Shape

if TYPE_CHECKING:
    from experience.mecmod_interfaces import Body

class BooleanShape(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         BooleanShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.boolean_shape = com

    def body(self) -> 'Body':
        from experience.mecmod_interfaces import Body
        return Body(self.boolean_shape.Body)

    def set_operated_object(self, i_reference_object: Reference) -> 'BooleanShape':
        self.boolean_shape.SetOperatedObject(i_reference_object._com)
        return self

    def set_operating_volume(self, i_reference_object: Reference) -> 'BooleanShape':
        self.boolean_shape.SetOperatingVolume(i_reference_object._com)
        return self

    def __repr__(self):
        return f'BooleanShape(name="{self.name()}")'