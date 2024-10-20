from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_mechanism_types import *
from experience.cat_kin_mechanism_interfaces.kin_command import KinCommand

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_kin_mechanism_interfaces.kin_mechanism import KinMechanism
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class KinSubCommand(KinCommand):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATKinMechanismIDLItf.KinCommand
                |                         KinSubCommand
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_sub_command = com

    def sub_mechanism(self) -> 'KinMechanism':
        from experience.cat_kin_mechanism_interfaces.kin_mechanism import KinMechanism
        return KinMechanism(self.kin_sub_command.SubMechanism)
    
    def sub_mechanism_product_occurrence(self) -> 'VPMOccurrence':
        from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence
        return VPMOccurrence(self.kin_sub_command.SubMechanismProductOccurrence)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'