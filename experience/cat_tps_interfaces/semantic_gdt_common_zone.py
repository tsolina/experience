from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import SemanticGDTCommonZone

class SemanticGDTCommonZone(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTCommonZone
    """

    def __init__(self, com):
        super().__init__(com)
        self.semantic_gdt_common_zone = com

    def modifier(self) -> str:
        return self.semantic_gdt_common_zone.Modifier

    def __repr__(self):
        return f'SemanticGDTCommonZone(name="{self.name()}")'