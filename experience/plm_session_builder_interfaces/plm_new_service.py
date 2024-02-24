from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.inf_interfaces import Editor

class PLMNewService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMNewService
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_new_service = com
    
    def plm_create(self, i_user_type: str) -> 'Editor':
        """
        3DShape: to create a 3D Representation 
        Drawing: to create a Drawing Representation
        """
        from experience.inf_interfaces import Editor
        return Editor(self.plm_new_service.PLMCreate(i_user_type)) 
    
    def plm_create_drawing(self) -> 'Editor':
        from experience.inf_interfaces import Editor
        return Editor(self.plm_new_service.PLMCreate('Drawing')) 
    
    def plm_create_3d_shape(self) -> 'Editor':
        from experience.inf_interfaces import Editor
        return Editor(self.plm_new_service.PLMCreate('3DShape')) 
    
    def set_attribute_value(self, i_attribute_id: str, i_attribute_value: 'cat_variant') -> 'PLMNewService':
        self.plm_new_service.SetAttributeValue(i_attribute_id, i_attribute_value)
        return self