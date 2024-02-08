from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class Thickness(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Thickness
    """

    def __init__(self, com):
        super().__init__(com)
        self.thickness = com

    def faces_to_thicken(self) -> References:
        return References(self.thickness.FacesToThicken)

    def offset(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.thickness.Offset)

    def add_face_to_thicken(self, i_face_to_thicken: Reference) -> 'Thickness':
        self.thickness.AddFaceToThicken(i_face_to_thicken._com)
        return self

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> 'Thickness':
        self.thickness.AddFaceWithDifferentThickness(i_face_to_thicken._com)
        return self

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> 'Thickness':
        self.thickness.RemoveFaceWithDifferentThickness(i_face_to_remove._com)
        return self

    def set_volume_support(self, i_volume_support: Reference) -> 'Thickness':
        self.thickness.SetVolumeSupport(i_volume_support.com)
        return self

    def withdraw_face_to_thicken(self, i_face_to_withdraw: Reference) -> 'Thickness':
        self.thickness.WithdrawFaceToThicken(i_face_to_withdraw._com)
        return self

    def __repr__(self):
        return f'Thickness(name="{self.name}")'