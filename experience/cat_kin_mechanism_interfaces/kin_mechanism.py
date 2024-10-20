from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_mechanism_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence
    from experience.cat_kin_mechanism_interfaces import KinCommands, KinJoints

class KinMechanism(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinMechanism
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_mechanism = com

    def commands(self) -> 'KinCommands':
        from experience.cat_kin_mechanism_interfaces.kin_commands import KinCommands
        return KinCommands(self.kin_mechanism.Commands)
    
    def joints(self) -> 'KinJoints':
        from experience.cat_kin_mechanism_interfaces.kin_joints import KinJoints
        return KinJoints(self.kin_mechanism.Joints)
    
    def mechanism_products(self) -> list['VPMOccurrence']:
        return self.kin_mechanism.MechanismProducts
    
    def attach_dressup_product(self, i_mechanism_product: 'VPMOccurrence', i_attached_product: 'VPMOccurrence') -> 'KinMechanism':
        self.kin_mechanism.AttachDressupProduct(i_mechanism_product._com, i_attached_product._com)
        return self
    
    def clean_simulation(self) -> 'KinMechanism':
        self.kin_mechanism.CleanSimulation()
        return self
    
    def detach_dressup_product(self, i_attached_product: 'VPMOccurrence') -> 'KinMechanism':
        self.kin_mechanism.DetachDressupProduct(i_attached_product._com)
        return self
    
    def get_dressup_products(self, i_mechanism_product: 'VPMOccurrence') -> list['VPMOccurrence']:
        return self.kin_mechanism.GetDressupProducts(i_mechanism_product._com)

    def prepare_simulation(self) -> 'KinMechanism':
        self.kin_mechanism.PrepareSimulation()
        return self
    
    def run_command(self, i_command: 'cat_variant', i_value: float) -> 'KinMechanism':
        self.kin_mechanism.RunCommand(i_command, i_value)
        return self
    
    def run_simulation(self, i_cmd_values: list) -> 'KinMechanism':
        self.kin_mechanism.RunSimulation(i_cmd_values)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'