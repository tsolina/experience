from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import DressUpShape

class RemoveFace(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             RemoveFace
    """

    def __init__(self, com):
        super().__init__(com)
        self.remove_face = com

    def keep_face(self, reference_face: Reference) -> "RemoveFace":
        self.remove_face.KeepFace = reference_face._com
        return self

    def keep_faces(self) -> References:
        return References(self.remove_face.KeepFaces)

    def propagation(self) -> References:
        return References(self.remove_face.Propagation)

    def remove_face(self, reference_face: Reference):
        self.remove_face.RemoveFace = reference_face._com
        return self

    def remove_faces(self) -> References:
        return References(self.remove_face.RemoveFaces)

    def remove_keep_face(self, i_keep_face: Reference) -> 'RemoveFace':
        self.remove_face.remove_KeepFace(i_keep_face._com)
        return self

    def remove_remove_face(self, i_remove_face: Reference) -> 'RemoveFace':
        self.remove_face.remove_RemoveFace(i_remove_face._com)
        return self

    def __repr__(self):
        return f'RemoveFace(name="{self.name}")'