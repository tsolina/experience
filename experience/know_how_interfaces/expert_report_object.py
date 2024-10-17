from experience.system import AnyObject

class ExpertReportObject(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertReportObject
    """

    def __init__(self, com):
        super().__init__(com)
        self.expert_report_object = com

    def validity(self) -> bool:
        return self.expert_report_object.Validity
    
    def get_tuple(self) -> tuple:
        return self._get_safe_array(self.expert_report_object, "getTuple", self.get_tuple_size())
    
    def get_tuple_size(self) -> int:
        return self.expert_report_object.getTupleSize()

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'