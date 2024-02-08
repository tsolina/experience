from typing import Union, Optional, TYPE_CHECKING

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

    def mode(self, value: int = None) -> Union['Chamfer', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Mode = value
            return self
        return self.chamfer.Mode

    def orientation(self, value: int = None) -> Union['Chamfer', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Orientation = value
            return self
        return self.chamfer.Orientation

    def propagation(self, value: int = None) -> Union['Chamfer', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.chamfer.Propagation = value
            return self
        return self.chamfer.Propagation

    def add_element_to_chamfer(self, i_element_to_chamfer: Reference) -> 'Chamfer':
        self.chamfer.AddElementToChamfer(i_element_to_chamfer._com)
        return self

    def withdraw_element_to_chamfer(self, i_element_to_withdraw: Reference) -> 'Chamfer':
        self.chamfer.WithdrawElementToChamfer(i_element_to_withdraw._com)
        return self

    def __repr__(self):
        return f'Chamfer(name="{self.name}")'