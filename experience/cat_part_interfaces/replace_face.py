from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import SurfaceBasedShape

class ReplaceFace(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             ReplaceFace
    """

    def __init__(self, com):
        super().__init__(com)
        self.replace_face = com

    def remove_face(self) -> References:
        return References(self.replace_face.RemoveFace)

    def splitting_side(self, value: int = None) -> Union['ReplaceFace', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.replace_face.SplittingSide = value
            return self
        return self.replace_face.SplittingSide

    def add_remove_face(self, i_remove_face: Reference) -> 'ReplaceFace':
        self.replace_face.AddRemoveFace(i_remove_face._com)
        return self

    def add_split_plane(self, i_split_plane: Reference) -> 'ReplaceFace':
        self.replace_face.AddSplitPlane(i_split_plane._com)
        return self

    def delete_remove_face(self, i_remove_face: Reference) -> 'ReplaceFace':
        self.replace_face.DeleteRemoveFace(i_remove_face._com)
        return self

    def __repr__(self):
        return f'ReplaceFace(name="{self.name()}")'