from experience.inf_interfaces import Service

class DrawingService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         DrawingService
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_service = com
    
    def number_of_standards(self) -> int:
        return self.drawing_service.NumberOfStandards
    
    def number_of_sheet_styles(self, i_standard_name: str) -> int:
        return self.drawing_service.NumberOfSheetStyles(i_standard_name)
    
    def sheet_style_names_list(self, i_standard_name: str) -> tuple:
        return self._get_safe_array(self.drawing_service, "SheetStyleNamesList", self.number_of_sheet_styles(), i_standard_name)
    
    def standard_names_list(self) -> tuple:
        return self._get_safe_array(self.drawing_service, "StandardNamesList", self.number_of_standards())

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'