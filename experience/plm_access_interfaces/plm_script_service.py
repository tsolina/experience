from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service


if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.plm_modeler_base_interfaces import PLMEntity

class PLMScriptService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMScriptService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_script_service = com
    
    def execute_script_v6(self, i_plm_entity: 'PLMEntity', i_type: int, i_program_name: str, i_function_name: str, i_parameters: tuple) -> 'cat_variant':
        """ i_type:
        enum CatScriptLibraryType {
        catScriptLibraryTypeDocument,
        catScriptLibraryTypeDirectory,
        catScriptLibraryTypeVBAProject,
        catScriptLibraryTypeVSTAProject
        }  
        """
        return self.plm_script_service.ExecuteScriptV6(i_plm_entity, i_type, i_program_name, i_function_name, i_parameters)  

    def __repr__(self):
        return f'PLMPlay(name="{self.name}")'