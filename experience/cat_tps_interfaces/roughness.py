from experience.system import AnyObject
from experience.cat_tps_interfaces import TPSParallelOnScreen

class Roughness(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Roughness
    """

    def __init__(self, com):
        super().__init__(com)
        self.roughness = com

    def applicability(self, value: int = None) -> int:
        if value is not None:
            self.roughness.Applicability = value
            return self
        return self.roughness.Applicability

    def obtention(self, value: int = None) -> int:
        if value is not None:
            self.roughness.Obtention = value
            return self
        return self.roughness.Obtention

    def field(self, i_index: int) -> str:
        return self.roughness.Field(i_index)

    def set_field(self, i_index: int, i_field: str) -> 'Roughness':
        self.roughness.SetField(i_index, i_field)
        return self


    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.roughness.TPSParallelOnScreen())