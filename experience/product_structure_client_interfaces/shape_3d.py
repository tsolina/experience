from typing import TYPE_CHECKING

from experience.system import AnyObject

class Shape3D(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Shape3D
    """

    def __init__(self, com):
        super().__init__(com)
        self.shape_3d = com

    def part(self) -> 'AnyObject':
        return AnyObject(self.shape_3d.Part)

    def __repr__(self):
        return f'Shape3D(name="{self.name}")'