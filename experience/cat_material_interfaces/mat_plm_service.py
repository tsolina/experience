from typing import Union, Optional, TYPE_CHECKING


from experience.system import AnyObject, Collection
from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.cat_material_interfaces import MaterialGeneric, AppliedMaterial, AppliedMaterials
    from experience.inf_interfaces.editor import Editor

class MATPLMService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         MATPLMService
    """

    def __init__(self, com):
        super().__init__(com)
        self.mat_plm_service = com
    
    def get_material_core(self, i_support: AnyObject) -> tuple["MaterialGeneric", "AppliedMaterial"]:
        rval = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "GetMaterialCore", "AnyObject"),
                               ["MaterialGeneric", "AppliedMaterial"])
        from experience.cat_material_interfaces import MaterialGeneric, AppliedMaterial
        return (MaterialGeneric(rval[0]), AppliedMaterial(rval[1]))
    
    def get_material_covering(self, i_support: AnyObject) -> tuple[Collection, "AppliedMaterials"]:
        rval = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "GetMaterialCovering", "AnyObject"),
                               ["Collection", "AppliedMaterials"])
        from experience.cat_material_interfaces import AppliedMaterials
        return (Collection(rval[0]), AppliedMaterials(rval[1]))
    
    def get_materials_in_session(self) -> Collection:
        return self.mat_plm_service.GetMaterialsInSession()
    
    def load_materials(self, i_vpm_reference: AnyObject, i_recursive: bool) -> 'MATPLMService':
        self.mat_plm_service.LoadMaterials(i_vpm_reference._com, i_recursive)
        return self
    
    def plm_create(self, i_user_type: str) -> tuple['MaterialGeneric', 'Editor']:
        rval = self._get_multi([self.mat_plm_service, i_user_type],
                               ("MATPLMService", "PLMCreate", "String"),
                               ["MaterialGeneric", "Editor"])
        
        from experience.cat_material_interfaces import MaterialGeneric
        from experience.inf_interfaces.editor import Editor
        return (MaterialGeneric(rval[0]), Editor(rval[1]))
    
    def remove_applied_material(self, i_applied_material: 'AppliedMaterial') -> 'MATPLMService':
        self.mat_plm_service.RemoveAppliedMaterial(i_applied_material)
        return self
    
    def set_display_msg_box(self, i_bool_display_msg_box: bool) -> 'MATPLMService':
        self.mat_plm_service.SetDisplayMsgBox(i_bool_display_msg_box)
        return self
    
    def set_material_core(self, i_support: AnyObject, i_core_material: 'MaterialGeneric') -> 'AppliedMaterial':
        rval = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "SetMaterialCore", "AnyObject"),
                               ["AppliedMaterial"])
        from experience.cat_material_interfaces import AppliedMaterial
        return AppliedMaterial(rval[0])
    
    def set_material_covering(self, i_support: AnyObject, i_core_material: 'MaterialGeneric') -> 'AppliedMaterial':
        rval = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "SetMaterialCovering", "AnyObject"),
                               ["AppliedMaterial"])
        from experience.cat_material_interfaces import AppliedMaterial
        return AppliedMaterial(rval[0])