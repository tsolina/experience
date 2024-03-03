from typing import TYPE_CHECKING

from experience.plm_modeler_base_interfaces.plm_entity import PLMEntity

if TYPE_CHECKING:
    from experience.cat_material_interfaces import MaterialDomainContent

class MaterialDomain(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         MaterialDomain
    """

    def __init__(self, com):
        super().__init__(com)
        self.material_domain = com

    def material_domain_content(self) -> 'MaterialDomainContent':
        from experience.cat_material_interfaces import MaterialDomainContent
        return MaterialDomainContent(self.material_domain.MaterialDomainContent())
