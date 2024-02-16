from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import Fillet

class TritangentFillet(Fillet):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 TritangentFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.tritangent_fillet = com

    def face_to_remove(self, value: Reference = None) -> Union['TritangentFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.tritangent_fillet.FaceToRemove = value._com
            return self
        return Reference(self.tritangent_fillet.FaceToRemove)

    def first_face(self, value: Reference = None) -> Union['TritangentFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.tritangent_fillet.FirstFace = value._com
            return self
        return Reference(self.tritangent_fillet.FirstFace)

    def second_face(self, value: Reference = None) -> Union['TritangentFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.tritangent_fillet.SecondFace = value._com
            return self
        return Reference(self.tritangent_fillet.SecondFace)

    def __repr__(self):
        return f'TritangentFillet(name="{ self.name() }")'