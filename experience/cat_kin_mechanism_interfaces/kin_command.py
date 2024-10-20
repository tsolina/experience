from typing import Iterator, TYPE_CHECKING, Union

from .cat_kin_mechanism_types import *

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_eng_connection_interfaces.eng_connection import EngConnection 

class KinCommand(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinCommand
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_command = com

    def command_type(self) -> CATKinMechanismCommandType:
        return CATKinMechanismCommandType.item(self.kin_command.CommandType)
    
    def current_value(self) -> float:
        return self.kin_command.CurrentValue
    
    def joint(self) -> 'EngConnection':
        from experience.cat_eng_connection_interfaces.eng_connection import EngConnection
        return EngConnection(self.kin_command.Joint)
    
    def lower_limit(self) -> float:
        return self.kin_command.LowerLimit
    
    def upper_limit(self) -> float:
        return self.kin_command.UpperLimit
    
    def is_lower_limit_set(self) -> bool:
        return self.kin_command.IsLowerLimitSet()
    
    def is_upper_limit_set(self) -> bool:
        return self.kin_command.IsUpperLimitSet()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'