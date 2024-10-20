from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMInstances, VPMPublications, VPMRepInstances
    from experience.cat_eng_connection_interfaces.eng_connections import EngConnections

class VPMReference(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMReference 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_reference = com

    def instances(self) -> 'VPMInstances':
        from experience.product_structure_client_interfaces import VPMInstances
        return VPMInstances(self.vpm_reference.Instances)

    def publications(self) -> 'VPMPublications':
        from experience.product_structure_client_interfaces import VPMPublications
        return VPMPublications(self.vpm_reference.Publications)  

    def rep_instances(self) -> 'VPMRepInstances':
        from experience.product_structure_client_interfaces import VPMRepInstances
        return VPMRepInstances(self.vpm_reference.RepInstances)  
    
    def plm_id(self) -> str:
        return self.get_attribute_value("PLM_ExternalID") # its settable too
    
    def eng_connections(self) -> 'EngConnections':
        from experience.cat_eng_connection_interfaces.eng_connections import EngConnections
        return self.get_item("CATEngConnections", EngConnections)

    def __repr__(self):
        return f'VPMReference(name="{self.name()}")'