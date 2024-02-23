from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.cat_part_types import *
from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class Chamfer(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Chamfer
    """

    def __init__(self, com):
        super().__init__(com)
        self.chamfer = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.chamfer.Angle)

    def elements_to_chamfer(self) -> References:
        return References(self.chamfer.ElementsToChamfer)

    def length1(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.chamfer.Length1)

    def length2(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.chamfer.Length2)

    def mode(self, value: CatChamferMode = None) -> Union['Chamfer', CatChamferMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Mode = int(value)
            return self
        return CatChamferMode.item(self.chamfer.Mode)

    def orientation(self, value: CatChamferOrientation = None) -> Union['Chamfer', CatChamferOrientation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Orientation = int(value)
            return self
        return CatChamferOrientation.item(self.chamfer.Orientation)

    def propagation(self, value: CatChamferPropagation = None) -> Union['Chamfer', CatChamferPropagation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Propagation = int(value)
            return self
        return CatChamferPropagation.item(self.chamfer.Propagation)

    def add_element_to_chamfer(self, i_element_to_chamfer: Reference) -> 'Chamfer':
        self.chamfer.AddElementToChamfer(i_element_to_chamfer._com)
        return self

    def withdraw_element_to_chamfer(self, i_element_to_withdraw: Reference) -> 'Chamfer':
        self.chamfer.WithdrawElementToChamfer(i_element_to_withdraw._com)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'