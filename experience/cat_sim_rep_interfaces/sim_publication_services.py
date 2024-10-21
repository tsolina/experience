from typing import Iterator, TYPE_CHECKING, Union

from experience.inf_interfaces.service import Service

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_reference import VPMReference
    from experience.product_structure_client_interfaces.vpm_publication import VPMPublication

class SimPublicationServices(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimPublicationServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_publication_service = com

    def create_publication(self, i_reference_product: 'VPMReference', i_link: AnyObject, i_publication_name: str) -> 'VPMPublication':
        from experience.product_structure_client_interfaces.vpm_publication import VPMPublication
        return VPMPublication(self.sim_publication_service.CreatePublication(i_reference_product._com, i_link._com, i_publication_name))
    
    def get_published_element(self, i_publication: 'VPMPublication') -> AnyObject:
        return AnyObject(self._get_multi([self.sim_publication_service, i_publication._com],
                         ("SimPublicationServices", 'GetPublishedElement', 'VPMPublication'),
                         ('AnyObject')))
        # return AnyObject(self.sim_publication_service.GetPublishedElement(i_publication._com))

    def modify_published_element(self, i_publication: 'VPMPublication', i_link: AnyObject) -> 'SimPublicationServices':
        self.sim_publication_service.ModifyPublishedElement(i_publication._com, i_link._com)
        return self
    
    def remove_publication(self, i_reference_product: 'VPMReference', i_publication: 'VPMPublication') -> 'SimPublicationServices':
        self.sim_publication_service.RemovePublication(self, i_reference_product._com, i_publication._com)
        return self
    
    def remove_publication_by_name(self, i_reference_product: 'VPMReference', i_publication_name: str) -> 'SimPublicationServices':
        self.sim_publication_service.RemovePublicationByName(i_reference_product._com, i_publication_name)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'