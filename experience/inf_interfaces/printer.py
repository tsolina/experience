from experience.system.any_object import AnyObject

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

    def orientation(self) -> int:
        return self.printer.Orientation

    def paper_height(self) -> float:
        return self.printer.PaperHeight

    def paper_size(self) -> int:
        return self.printer.PaperSize

    def paper_width(self) -> float:
        return self.printer.PaperWidth

    def __repr__(self):
        return f'Printer(name="{self.name}")'
