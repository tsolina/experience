from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import DressUpShape

class Fillet(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Fillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.fillet = com

    def fillet_boundary_relimitation(self, value: CatFilletBoundaryRelimitation = None) -> Union['Fillet', CatFilletBoundaryRelimitation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.fillet.FilletBoundaryRelimitation = int(value)
            return self
        return CatFilletBoundaryRelimitation.item(self.fillet.FilletBoundaryRelimitation)

    def fillet_trim_support(self, value: CatFilletTrimSupport = None) -> Union['Fillet', CatFilletTrimSupport]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.fillet.FilletTrimSupport = int(value)
            return self
        return CatFilletTrimSupport.item(self.fillet.FilletTrimSupport)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'