from experience.system.any_object import AnyObject
from experience.types.general import cat_variant

class SystemService(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SystemService
    """

    def __init__(self, com):
        super().__init__(com)
        self.system_service = com

    def environ(self, i_env_string) -> str:
        return str(self.system_service.Environ(i_env_string))

    def evaluate(self, i_script_text: str, i_language: int, i_function_name: str, i_parameters: list) -> 'cat_variant':
        return self.system_service.Evaluate(i_script_text, i_language, i_function_name, i_parameters)

    def execute_background_processus(self, i_executable_path) -> int:
        return int(self.system_service.ExecuteBackgroundProcessus(i_executable_path))

    def execute_processus(self, i_executable_path) -> int:
        return int(self.system_service.ExecuteProcessus(i_executable_path))

    # def execute_script(self, i_library_name: str, i_type: int, i_program_name: str, i_function_name: str, i_parameters: list):
    #     return self.system_service.ExecuteScript(i_library_name, i_type, i_program_name, i_function_name, i_parameters)

# TODO: check if all is correct
    def get_message(self, i_catalog_name: str, i_message_key: str, i_msg_parameters: tuple, i_default_msg: str) -> str:
        return str(self.system_service.GetMessage(i_catalog_name, i_message_key, i_msg_parameters, i_default_msg))

# deprecated
    def print(self, i_string) -> 'SystemService':
        self.system_service.Print(i_string)
        return self

    def print_to_stdout(self, i_string: str) -> 'SystemService':
        self.system_service.PrintToStdout(i_string)
        return self

    def __repr__(self):
        return f'SystemService(name="{self.name}")'
