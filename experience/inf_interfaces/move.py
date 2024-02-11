from typing import TYPE_CHECKING, Type, TypeVar, Optional
from experience.system import AnyObject

class Move(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Move
    """

    def __init__(self, com):
        super().__init__(com)
        self.move = com

    def movable_object(self) -> 'Move':
        return Move(self.move.MovableObject)

    def apply(self, i_transformation_array: tuple) -> 'Move':
        ''' - array(11), x(3), y(3), z(3), pos(3) - '''
        self.move.Apply(i_transformation_array)
        return self

    def __repr__(self):
        return f'Move(name="{self.name()}")'
