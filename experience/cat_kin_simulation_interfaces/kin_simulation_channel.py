from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_simulation_types import *
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.product_structure_client_interfaces.vpm_occurence import VPMOccurrence

class KinSimulationChannel(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinSimulationChannel
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_simulation_channel = com

    def channel_size(self) -> int:
        return self.kin_simulation_channel.ChannelSize
    
    def channel_type(self) -> CatKinSimuChannelType:
        return CatKinSimuChannelType.item(self.kin_simulation_channel.ChannelType)
    
    def channel_unit(self) -> str:
        return self.kin_simulation_channel.ChannelUnit
    
    def get_channel_value(self, i_index: int) -> tuple[float, bool]:
        return self._get_multi([self.kin_simulation_channel, i_index], ("KinSimulationChannel", "GetChannelValue", "Long"), ("Double", "Boolean"))
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'