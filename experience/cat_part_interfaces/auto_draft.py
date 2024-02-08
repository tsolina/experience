from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces.dress_up_shape import DressUpShape

class AutoDraft(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             AutoDraft
    """

    def __init__(self, com):
        super().__init__(com)
        self.auto_draft = com

    def functional_face(self, value: Reference = None) -> Union['AutoDraft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_draft.FunctionalFace = value._com
            return self
        return Reference(self.auto_draft.FunctionalFace)

    def functional_faces(self) -> References:
        return References(self.auto_draft.FunctionalFaces)

    def main_draft_angle(self, value: Reference = None) -> Union['AutoDraft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_draft.MainDraftAngle = value._com
            return self
        return Reference(self.auto_draft.MainDraftAngle)

    def mode(self, value: Reference = None) -> Union['AutoDraft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_draft.Mode = value._com
            return self
        return Reference(self.auto_draft.Mode)

    def parting_element(self, value: Reference = None) -> Union['AutoDraft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_draft.PartingElement = value._com
            return self
        return Reference(self.auto_draft.PartingElement)

    def pulling_direction(self, value: Reference = None) -> Union['AutoDraft', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_draft.PullingDirection = value._com
            return self
        return Reference(self.auto_draft.PullingDirection)

    def __repr__(self):
        return f'AutoDraft(name="{self.name}")'