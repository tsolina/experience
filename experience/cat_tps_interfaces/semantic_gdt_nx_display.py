from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_tps_interfaces import SemanticGDTCommonZone

class SemanticGDTNxDisplay(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTNxDisplay
    """

    def __init__(self, com):
        super().__init__(com)
        self.semantic_gdt_nx_display = com

    def instance_count(self) -> int:
        return self.semantic_gdt_nx_display.InstanceCount
    
    def common_zone(self) -> 'SemanticGDTCommonZone':
        from experience.cat_tps_interfaces import SemanticGDTCommonZone
        return SemanticGDTCommonZone(self.semantic_gdt_nx_display.CommonZone())
    
    def is_a_collection(self) -> bool:
        return self.semantic_gdt_nx_display.IsACollection()
    
    def is_a_separate(self) -> bool:
        return self.semantic_gdt_nx_display.IsASeparate()