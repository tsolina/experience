from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_rep_reference import VPMRepReference

class SimPrdRepFactory(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPrdRepFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_prd_rep_factory = com

    def create_prd_rep(self, i_rep_type: str) -> 'VPMRepReference':
        '''
        Legal values: "FEM", "XRep", or "AbstractionShape" 
        '''
        return VPMRepReference(self.sim_prd_rep_factory.CreatePrdRep(i_rep_type))
    
    def create_prd_rep_fem(self) -> 'VPMRepReference':
        return VPMRepReference(self.create_prd_rep("FEM"))
    
    def create_prd_rep_xrep(self) -> 'VPMRepReference':
        return VPMRepReference(self.create_prd_rep("XRep"))
    
    def create_prd_rep_abstraction_shape(self) -> 'VPMRepReference':
        return VPMRepReference(self.create_prd_rep("AbstractionShape"))   
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'