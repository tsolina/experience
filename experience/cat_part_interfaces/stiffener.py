from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import SketchBasedShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class Stiffener(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Stiffener
    """

    def __init__(self, com):
        super().__init__(com)
        self.stiffener = com

    def is_from_top(self, value: bool = None) -> Union['Stiffener', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.stiffener.IsFromTop = value
            return self
        return self.stiffener.IsFromTop

    def is_symmetric(self, value: bool = None) -> Union['Stiffener', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.stiffener.IsSymmetric = value
            return self
        return self.stiffener.IsSymmetric

    def thickness(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.stiffener.Thickness)

    def thickness_from_top(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.stiffener.ThicknessFromTop)

    def reverse_depth(self) -> 'Stiffener':
        self.stiffener.ReverseDepth()
        return self

    def reverse_thickness(self) -> 'Stiffener':
        self.stiffener.ReverseThickness()
        return self

    def __repr__(self):
        return f'Stiffener(name="{ self.name() }")'