from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import SketchBasedShape

class SolidCombine(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             SolidCombine
    """

    def __init__(self, com):
        super().__init__(com)
        self.solid_combine = com

    def first_component_direction(self, value: Reference = None) -> Union['SolidCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.solid_combine.FirstComponentDirection = value._com
            return self
        return Reference(self.solid_combine.FirstComponentDirection)

    def first_component_profile(self, value: Reference = None) -> Union['SolidCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.solid_combine.FirstComponentProfile = value._com
            return self
        return Reference(self.solid_combine.FirstComponentProfile)

    def second_component_direction(self, value: Reference = None) -> Union['SolidCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.solid_combine.SecondComponentDirection = value._com
            return self
        return Reference(self.solid_combine.SecondComponentDirection)

    def second_component_profile(self, value: Reference = None) -> Union['SolidCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.solid_combine.SecondComponentProfile = value._com
            return self
        return Reference(self.solid_combine.SecondComponentProfile)

    def __repr__(self):
        return f'SolidCombine(name="{ self.name }")'