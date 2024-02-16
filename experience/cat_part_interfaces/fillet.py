from typing import Union, Optional, TYPE_CHECKING

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

    def fillet_boundary_relimitation(self, value: int = None) -> Union['Fillet', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.fillet.FilletBoundaryRelimitation = value
            return self
        return self.fillet.FilletBoundaryRelimitation

    def fillet_trim_support(self, value: int = None) -> Union['Fillet', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.fillet.FilletTrimSupport = value
            return self
        return self.fillet.FilletTrimSupport

    def __repr__(self):
        return f'Fillet(name="{self.name()}")'