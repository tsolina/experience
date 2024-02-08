from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class Shell(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Shell
    """

    def __init__(self, com):
        super().__init__(com)
        self.shell = com

    def external_thickness(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.shell.ExternalThickness)

    def faces_to_remove(self) -> References:
        return References(self.shell.FacesToRemove)

    def internal_thickness(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.shell.InternalThickness)

    def add_face_to_remove(self, i_face_to_remove: Reference) -> 'Shell':
        self.shell.AddFaceToRemove(i_face_to_remove._com)
        return self

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> 'Shell':
        self.shell.AddFaceWithDifferentThickness(i_face_to_thicken._com)
        return self

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> 'Shell':
        self.shell.RemoveFaceWithDifferentThickness(i_face_to_remove._com)
        return self

    def set_volume_support(self, i_volume_support: Reference) -> 'Shell':
        self.shell.SetVolumeSupport(i_volume_support._com)
        return self

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> 'Shell':
        self.shell.WithdrawFaceToRemove(i_face_to_withdraw._com)
        return self

    def __repr__(self):
        return f'Shell(name="{self.name}")'