from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.system import AnyObject
from experience.cat_part_interfaces.cat_part_types import *

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle

class DraftDomain(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DraftDomain
    """

    def __init__(self, com):
        super().__init__(com)
        self.draft_domain = com

    def draft_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.draft_domain.DraftAngle)

    def faces_to_draft(self) -> References:
        return References(self.draft_domain.FacesToDraft)

    def multiselection_mode(self, value: CatDraftMultiselectionMode = None) -> Union['DraftDomain', CatDraftMultiselectionMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft_domain.MultiselectionMode = int(value)
            return self
        return CatDraftMultiselectionMode.item(self.draft_domain.MultiselectionMode)

    def neutral_element(self, value: Reference = None) -> Union['DraftDomain', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft_domain.NeutralElement = value._com
            return self
        return Reference(self.draft_domain.NeutralElement)

    def neutral_propagation_mode(self, value: CatDraftNeutralPropagationMode = None) -> Union['DraftDomain', CatDraftNeutralPropagationMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft_domain.NeutralPropagationMode = int(value)
            return self
        return CatDraftNeutralPropagationMode.item(self.draft_domain.NeutralPropagationMode)

    def pulling_direction_element(self, value: Reference = None) -> Union['DraftDomain', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.draft_domain.PullingDirectionElement = value._com
            return self
        return Reference(self.draft_domain.PullingDirectionElement)

    def add_face_to_draft(self, i_face: Reference) -> 'DraftDomain':
        self.draft_domain.AddFaceToDraft(i_face._com)
        return self

    def get_pulling_direction(self, io_pulling_direction: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetPullingDirection", 2)

    def remove_face_to_draft(self, i_face: Reference) -> 'DraftDomain':
        self.draft_domain.RemoveFaceToDraft(i_face._com)
        return self

    def set_pulling_direction(self, i_x: float, i_y: float, i_z: float) -> 'DraftDomain':
        self.draft_domain.SetPullingDirection(i_x, i_y, i_z)
        return self

    def set_volume_support(self, i_volume_support: Reference) -> 'DraftDomain':
        self.draft_domain.SetVolumeSupport(i_volume_support._com)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'