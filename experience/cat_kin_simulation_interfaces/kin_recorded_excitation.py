from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_kin_mechanism_interfaces.kin_command import KinCommand

class KinRecordedExcitation(SimExcitation): #'SimExcitation'
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATSimRepIDLItf.SimExcitation
                |                         KinRecordedExcitation
    """

    def __init__(self, com):
        super().__init__(com)
        self.kin_recorded_excitation = com

    def key_frames_size(self) -> int:
        return self.kin_recorded_excitation.KeyFramesSize
    
    def get_key_frames_times(self) -> list[float]:
        return self._get_safe_array(self.kin_recorded_excitation, "GetKeyFramesTimes", self.key_frames_size - 1)
    
    def get_key_frames_values(self, i_kin_cmd: 'KinCommand') -> list:
        #return self._get_multi([self.kin_recorded_excitation, i_kin_cmd._com], ("KinRecordedExcitation", "GetKeyFramesValues", "KinCommand"), ("Double"))
        vba_function_name = "func"
        vba_code = f"""
            Public Function {vba_function_name}(obj As KinRecordedExcitation, kin_cmd As KinCommand) As Variant
                Dim times() As Double
                Redim Times(obj.KeyFrameSize - 1)
                obj.GetKeyFramesValues kin_cmd, times
                {vba_function_name} = Array(times)
            End Function
        """

        from experience.system.system_types import CATScriptLanguage
        return self.application().system_service().evaluate(vba_code, CATScriptLanguage.CATVBScriptLanguage, vba_function_name, [self.kin_recorded_excitation, i_kin_cmd._com])
    
    def set_key_frames_times(self, i_times: list[float]) -> 'KinRecordedExcitation':
        self.kin_recorded_excitation.SetKeyFramesTimes(i_times)
        return self
    
    def set_key_frames_values(self, i_kin_cmd: 'KinCommand', i_values: list[float]) -> 'KinRecordedExcitation':
        self.kin_recorded_excitation.SetKeyFramesValues(i_kin_cmd._com, i_values)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'