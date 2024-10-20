from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_mechanism_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class KinDressup(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinDressup
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_dressup = com

    def mechanism_products(self) -> tuple:
        return self.kin_dressup.MechanismProducts
    
    def attach_dressup_product(self, i_mechanism_support: 'VPMOccurrence', i_attached_product: 'VPMOccurrence') -> 'KinDressup':
        self.kin_dressup.AttachDressupProduct(i_mechanism_support._com, i_attached_product._com)
        return self
    
    def detach_dressup_product(self, i_attached_product: 'VPMOccurrence') -> 'KinDressup':
        self.kin_dressup.DetachDressupProduct(i_attached_product._com)
        return self
    
    def get_dressup_products(self, i_mechanism_product: 'VPMOccurrence') -> list['VPMOccurrence']:
        return self.kin_dressup.GetDressupProducts(i_mechanism_product._com)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'