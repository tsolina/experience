from experience.system import AnyObject

class PrintArea(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PrintArea
    """

    def __init__(self, com):
        super().__init__(com)
        self.print_area = com

    def activation_state(self, value: bool = None) -> bool:
        if value is not None:
            self.print_area.ActivationState = value
            return self
        return self.print_area.ActivationState

    def area_height(self) -> float:
        if value is not None:
            self.print_area.AreaHeight = value
            return self
        return self.print_area.AreaHeight

    def area_low_x(self, value: float = None) -> float:
        if value is not None:
            self.print_area.AreaLowX = value
            return self
        return self.print_area.AreaLowX

    def area_low_y(self, value: float = None) -> float:
        if value is not None:
            self.print_area.AreaLowY = value
            return self
        return self.print_area.AreaLowY

    def area_width(self, value: float = None) -> float:
        if value is not None:
            self.print_area.AreaWidth = value
            return self
        return self.print_area.AreaWidth

    def get_area(self, o_x: float, o_y: float, o_width: float, o_height: float, o_activated: bool) -> tuple:
        return self.print_area.GetArea(o_x, o_y, o_width, o_height, o_activated)

    def set_area(self, i_x: float, i_y: float, i_width: float, i_height: float) -> 'PrintArea':
        self.print_area.SetArea(i_x, i_y, i_width, i_height)
        return self
        
    def __repr__(self):
        return f'PrintArea(name="{ self.name }")'
