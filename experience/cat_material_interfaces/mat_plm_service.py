from typing import Union, Optional, TYPE_CHECKING


from experience.system import AnyObject, Collection
from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.cat_material_interfaces import MaterialGeneric, AppliedMaterial, AppliedMaterials, ListObject
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
        gen, mat = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "GetMaterialCore", "AnyObject"),
                               ["MaterialGeneric", "AppliedMaterial"])
        from experience.cat_material_interfaces import MaterialGeneric, AppliedMaterial
        return (MaterialGeneric(gen) if gen is not None else None,
                AppliedMaterial(mat) if mat is not None else None)
    
    def get_material_covering(self, i_support: AnyObject) -> tuple[Collection, "AppliedMaterials"]:
        col, mats = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "GetMaterialCovering", "AnyObject"),
                               ["Collection", "AppliedMaterials"])
        from experience.cat_material_interfaces import AppliedMaterials
        return (Collection(col) if col is not None else None,
                AppliedMaterials(mats) if mats is not None else None)
    
    def get_materials_in_session(self) -> 'ListObject':
        mat_com = self._get_multi([self.mat_plm_service], ("MATPLMService","GetMaterialsInSession"), ["ListObject"])[0]

        from experience.cat_material_interfaces import ListObject
        return ListObject(mat_com) if mat_com is not None else None
    
    def load_materials(self, i_vpm_reference: AnyObject, i_recursive: bool) -> 'MATPLMService':
        self.mat_plm_service.LoadMaterials(i_vpm_reference._com, i_recursive)
        return self
    
    def plm_create(self, i_user_type: str) -> tuple['MaterialGeneric', 'Editor']:
        gen, edit = self._get_multi([self.mat_plm_service, i_user_type],
                               ("MATPLMService", "PLMCreate", "String"),
                               ["MaterialGeneric", "Editor"])
        
        from experience.cat_material_interfaces import MaterialGeneric
        from experience.inf_interfaces.editor import Editor
        return (MaterialGeneric(gen), Editor(edit))
    
    def remove_applied_material(self, i_applied_material: 'AppliedMaterial') -> 'MATPLMService':
        self.mat_plm_service.RemoveAppliedMaterial(i_applied_material._com)
        return self
    
    def set_display_msg_box(self, i_bool_display_msg_box: bool) -> 'MATPLMService':
        self.mat_plm_service.SetDisplayMsgBox(i_bool_display_msg_box)
        return self
    
    def set_material_core(self, i_support: AnyObject, i_core_material: 'MaterialGeneric') -> 'AppliedMaterial':
        rval = self._get_multi([self.mat_plm_service, i_support._com],
                               ("MATPLMService", "SetMaterialCore", "AnyObject"),
                               ["AppliedMaterial"])[0]
        from experience.cat_material_interfaces import AppliedMaterial
        return AppliedMaterial(rval)
    
    def set_material_covering(self, i_support: AnyObject, i_core_material: 'MaterialGeneric') -> 'AppliedMaterial':
        rval = self._get_multi([self.mat_plm_service, i_support._com, i_core_material._com],
                               ("MATPLMService", "SetMaterialCovering", "AnyObject", "MaterialGeneric"),
                               ["AppliedMaterial"])[0]
        from experience.cat_material_interfaces import AppliedMaterial
        return AppliedMaterial(rval)