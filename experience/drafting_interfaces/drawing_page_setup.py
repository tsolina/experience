from experience.inf_interfaces import PageSetup

class DrawingPageSetup(PageSetup):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.PageSetup
                |                         DrawingPageSetup
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_page_setup = com

    def choose_best_orientation(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_page_setup.ChooseBestOrientation = value
            return self
        return self.drawing_page_setup.ChooseBestOrientation

    def fit_to_printer_format(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_page_setup.FitToPrinterFormat = value
            return self
        return self.drawing_page_setup.FitToPrinterFormat

    def fit_to_sheet_format(self, value: bool = None) -> bool:
        if value is not None:
            self.drawing_page_setup.FitToSheetFormat = value
            return self
        return self.drawing_page_setup.FitToSheetFormat

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
