from typing import Union, Optional, TYPE_CHECKING

from experience.plm_modeler_base_interfaces import PLMEntity

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces import VPMReference, ParentVPMRepInstances
    from experience.mecmod_interfaces import Part
    from experience.knowledge_interfaces import KnowledgeObjects
    from experience.cat_kin_mechanism_interfaces.kin_mechanism import KinMechanism
    from experience.cat_sim_rep_interfaces.sim_rep_initialization import SimRepInitialization

class VPMRepReference(PLMEntity):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                |                       VPMRepReference 
    """

    def __init__(self, com):
        super().__init__(com)
        self.vpm_rep_reference = com

    def father(self) -> 'VPMReference':
        from experience.product_structure_client_interfaces import VPMReference
        return VPMReference(self.vpm_rep_reference.Father)

    def parent_rep_instances(self) -> 'ParentVPMRepInstances':
        from experience.product_structure_client_interfaces import ParentVPMRepInstances
        return VPMReference(self.vpm_rep_reference.ParentRepInstances)
    
    def part(self) -> 'Part':
        from experience.mecmod_interfaces import Part
        return self.get_item("Part", Part)
    
    def knowledge_objects(self) -> 'KnowledgeObjects':
        from experience.knowledge_interfaces import KnowledgeObjects
        return KnowledgeObjects(self.vpm_rep_reference.GetItem("KnowledgeObjects"))
    
    def kin_mechanism(self) -> 'KinMechanism':
        from experience.cat_kin_mechanism_interfaces.kin_mechanism import KinMechanism
        return self.get_item("MECHRep", KinMechanism)
    
    def is_machanism(self) -> bool:
        return self.get_attribute_value("V_discipline") == "Mechanism"
    
    def sim_rep_initialization(self) -> 'SimRepInitialization':
        from experience.cat_sim_rep_interfaces.sim_rep_initialization import SimRepInitialization
        return self.get_item('SimRepInitialization', SimRepInitialization)        

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
    
#  Dim MyRepRef as VPMRepReference
#  Set MyRepRef = ...
#  Dim disAttr As  String
#  disAttr = MyRepRef.GetAttributeValue("V_discipline")
#  If ( attr = "Mechanism" ) Then
#    Dim MyMECHRoot As KinMechanism
#    Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
#    Dim MyCommands As KinCommands
#    Set MyCommands = MyMECHRoot.Parameters
#  End If 