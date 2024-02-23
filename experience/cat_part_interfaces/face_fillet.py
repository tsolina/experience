from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.cat_part_interfaces.fillet import Fillet

if TYPE_CHECKING:
    from experience.knowledge_interfaces.length import Length

class FaceFillet(Fillet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 FaceFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.face_fillet = com

    def first_face(self, value: Reference = None) -> Union['FaceFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.face_fillet.FirstFace = value._com
            return self
        return Reference(self.face_fillet.FirstFace)

    def radius(self) -> 'Length':
        from experience.knowledge_interfaces.length import Length
        return Length(self.face_fillet.Radius)

    def second_face(self, value: Reference = None) -> Union['FaceFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.face_fillet.SecondFace = value._com
            return self
        return Reference(self.face_fillet.SecondFace)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'