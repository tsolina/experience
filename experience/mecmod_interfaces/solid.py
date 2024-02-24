from typing import TYPE_CHECKING
from experience.mecmod_interfaces import Shape

if TYPE_CHECKING:
    from experience.inf_interfaces import Move

class Solid(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         Solid
    """

    def __init__(self, com):
        super().__init__(com)
        self.solid = com

    def move(self) -> 'Move':
        from experience.inf_interfaces import Move
        return Move(self.solid.Move)