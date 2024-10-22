from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.knowledge_interfaces.real_param import RealParam

class FreeParameter(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FreeParameter
    """

    def __init__(self, com):
        super().__init__(com)
        self.free_parameter = com

    def inf_range(self) -> float:
        return self.free_parameter.InfRange
    
    def parameter(self) -> 'RealParam':
        from experience.knowledge_interfaces.real_param import RealParam
        return RealParam(self.free_parameter.Parameter)
    
    def step(self) -> float:
        return self.free_parameter.Step
    
    def sup_range(self) -> float:
        return self.free_parameter.SupRange
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'