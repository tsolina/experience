from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant

class PLMEntity(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_entity = com

    def get_attribute_value(self, i_attr_name: str) -> 'cat_variant':
        try:
            return self.plm_entity.GetAttributeValue(i_attr_name)
        except Exception as e:
            return i_attr_name + " not found!"

    def has_attribute_value(self, i_attr_name: str) -> bool:
        try:
            val = self.plm_entity.GetAttributeValue(i_attr_name)
            return True
        except Exception as e:
            return False

    def get_custom_type(self) -> str:
        return self.plm_entity.GetCustomType()
    
    def set_attribute_value(self, i_attr_name, i_attr_value: 'cat_variant') -> 'PLMEntity':
        self.plm_entity.SetAttributeValue(i_attr_name, i_attr_value)
        return self
    
    def title(self, value: str = None) -> Union['PLMEntity', str]:
        if value is not None:
            self.set_attribute_value("V_Name", value) # "PLM_ExternalID"
            return self
        return self.get_attribute_value("V_Name")
    
    def id(self, value: str = None) -> Union['PLMEntity', str]:
        if value is not None:
            self.set_attribute_value("PLM_ExternalID", value)
            return self
        return self.get_attribute_value("PLM_ExternalID")
    
    def revision(self, value: str = None) -> Union['PLMEntity', str]:
        if value is not None:
            self.set_attribute_value("revision", value)
            return self
        return self.get_attribute_value("revision")
    
    