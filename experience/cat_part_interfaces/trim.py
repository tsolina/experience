from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import BooleanShape

class Trim(BooleanShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Trim
    """

    def __init__(self, com):
        super().__init__(com)
        self.trim = com

    def add_face_to_keep(self, i_face_to_keep: Reference) -> 'Trim':
        self.trim.AddFaceToKeep(i_face_to_keep._com)
        return self

    def add_face_to_keep2(self, i_face_to_keep: Reference, i_face_adjacent_for_keep: Reference) -> 'Trim':
        self.trim.AddFaceToKeep2(i_face_to_keep._com, i_face_adjacent_for_keep._com)
        return self

    def add_face_to_remove(self, i_face_to_remove: Reference) -> 'Trim':
        self.trim.AddFaceToRemove(i_face_to_remove._com)
        return self

    def add_face_to_remove2(self, i_face_to_remove: Reference, i_face_adjacent_for_remove: Reference) -> 'Trim':
        self.trim.AddFaceToRemove2(i_face_to_remove._com, i_face_adjacent_for_remove._com)
        return self

    def withdraw_face_to_keep(self, i_face_to_withdraw: Reference) -> 'Trim':
        self.trim.WithdrawFaceToKeep(i_face_to_withdraw._com)
        return self

    def withdraw_face_to_keep2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_keep: Reference) -> 'Trim':
        self.trim.WithdrawFaceToKeep2(i_face_to_withdraw._com, i_face_adjacent_for_keep._com)
        return self

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> 'Trim':
        self.trim.WithdrawFaceToRemove(i_face_to_withdraw._com)
        return self

    def withdraw_face_to_remove2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_remove: Reference) -> 'Trim':
        self.trim.WithdrawFaceToRemove2(i_face_to_withdraw._com, i_face_adjacent_for_remove._com)
        return self

    def __repr__(self):
        return f'Trim(name="{self.name()}")'