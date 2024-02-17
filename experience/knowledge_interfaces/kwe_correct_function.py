from experience.system import AnyObject

class KWECorrectFunction(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KWECorrectFunction
    """

    def __init__(self, com):
        super().__init__(com)
        self.kwe_correct_function = com

    def check(self) -> AnyObject:
        return AnyObject(self.kwe_correct_function.Check())

    def get_number_of_list_failed_elements(self) -> int:
        return self.kwe_correct_function.GetNumberOfListFailedElements()
    
    def list_failed_elements(self) -> tuple:
        return self._get_safe_array(self.kwe_correct_function, "ListFailedElements", self.get_number_of_list_failed_elements())

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'