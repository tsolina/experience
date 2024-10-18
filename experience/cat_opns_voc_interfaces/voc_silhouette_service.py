from typing import Union, TYPE_CHECKING

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_reference import VPMReference

class VOCSilhouetteService(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VOCSilhouetteService
    """

    def __init__(self, com):
        super().__init__(com)
        self.voc_silhouette_service = com

    def create_a_silhouette(self, i_products_to_treat: list, i_product_reference: VPMReference, i_list_of_view_points: list, i_silhouette_acc: float,
                            i_accuracy_for_simplification: float) -> 'VOCSilhouetteService':
        '''
        Deprecated: 
        R2020x Use CATEVOCServices::ComputeASilhouette (VOCServices.ComputeASilhouette) Compute a Silhouette. 
        '''
        self.voc_silhouette_service.CreateASilhouette(i_products_to_treat, i_product_reference._com, i_list_of_view_points, i_silhouette_acc, i_accuracy_for_simplification)
        return self        

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'