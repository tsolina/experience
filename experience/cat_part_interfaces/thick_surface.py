from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import SurfaceBasedShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class ThickSurface(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             ThickSurface
    """

    def __init__(self, com):
        super().__init__(com)
        self.thick_surface = com

    def bot_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.thick_surface.BotOffset)

    def offset_side(self) -> int:
        return self.thick_surface.OffsetSide

    def top_offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.thick_surface.TopOffset)

    def swap_offset_side(self) -> 'ThickSurface':
        self.thick_surface.swap_OffsetSide()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'