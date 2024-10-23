from experience.system import AnyObject

class SIMDynClashResult(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SIMDynClashResult
    """

    def __init__(self, com):
        super().__init__(com)
        self.sym_dyn_clash_result = com

    def clash_type(self) -> int:
        return self.sym_dyn_clash_result.ClashType
    
    def get_colliding_part(self, i_index: int) -> AnyObject:
        return AnyObject(self.sym_dyn_clash_result.GetCollidingPart(i_index))
    
    def get_parameter(self, i_parameter_id: str) -> float:
        return self.sym_dyn_clash_result.GetParameter(i_parameter_id)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'