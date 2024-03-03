from typing import TYPE_CHECKING

from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.cat_material_interfaces import MaterialBehaviorOptions

class MaterialBehavior(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         MaterialBehavior
    """

    def __init__(self, com):
        super().__init__(com)
        self.material_behavior = com

    def get_domains(self) -> 'MaterialBehaviorOptions':
        from experience.cat_material_interfaces import MaterialBehaviorOptions
        return MaterialBehaviorOptions(self.material_behavior.BehaviorOptions())
