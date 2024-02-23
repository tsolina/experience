from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import SurfaceBasedShape

class Split(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             Split
    """

    def __init__(self, com):
        super().__init__(com)
        self.split = com

    def splitting_side(self, value: CatSplitSide = None) -> Union['Split', CatSplitSide]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.split.SplittingSide = int(value)
            return self
        return CatSplitSide.item(self.split.SplittingSide)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'