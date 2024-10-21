from experience.cat_behavior_interfaces.dpc_operation import DPCOperation
from experience.system import AnyObject

class DPCOperationVBScript(DPCOperation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATBehaviorIDLItf.DPCOperation
                |                         DPCOperationVBScript
    """

    def __init__(self, com):
        super().__init__(com)
        self.dpc_operation_vbscript = com

    def get_input(self, p_name: str) -> AnyObject:
        return AnyObject(self.dpc_operation_vbscript.GetInput(p_name))
    
    def get_internal(self, p_name: str) -> AnyObject:
        return AnyObject(self.dpc_operation_vbscript.GetInternal(p_name))
    
    def get_output(self, p_name: str) -> AnyObject:
        return AnyObject(self.dpc_operation_vbscript.GetOutput(p_name))
    
    def put_internal(self, p_name: str, i_value: AnyObject) -> 'DPCOperationVBScript':
        self.dpc_operation_vbscript.PutInternal(p_name, i_value._com)
        return self
    
    def put_output(self, p_name: str, i_value: AnyObject) -> 'DPCOperationVBScript':
        self.dpc_operation_vbscript.PutOutput(p_name, i_value._com)
        return self
    
    def test_input(self, p_name: str) -> int:
        return self.dpc_operation_vbscript.TestInput(p_name)
    
    def test_internal(self, p_name: str) -> int:
        return self.dpc_operation_vbscript.TestInternal(p_name)
    
    def test_output(self, p_name: str) -> int:
        return self.dpc_operation_vbscript.TestOutput(p_name)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'