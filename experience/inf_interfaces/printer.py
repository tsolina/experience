from experience.system import AnyObject

from experience.inf_interfaces.inf_types import *

class Printer(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Printer
    """

    def __init__(self, com):
        super().__init__(com)
        self.printer = com

    def device_name(self) -> str:
        return self.printer.DeviceName

    def orientation(self) -> CatPaperOrientation:
        return CatPaperOrientation.item(self.printer.Orientation)

    def paper_height(self) -> float:
        return self.printer.PaperHeight

    def paper_size(self) -> CatPaperSize:
        return CatPaperSize.item(self.printer.PaperSize)

    def paper_width(self) -> float:
        return self.printer.PaperWidth

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'