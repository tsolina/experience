from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

from experience.drafting_2d_interfaces.drafting_2d_types import CatVisuIn3DMode
from experience.inf_interfaces.inf_types import CatRenderingMode

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Parameters, Relations    
    from experience.drafting_2d_interfaces import Layout2DSheet, Layout2DSheets, Layout2DServices

class Layout2DRoot(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DRoot
    """

    def __init__(self, com):
        super().__init__(com)
        self.layout_2d_root = com

    def active_sheet(self, value: 'Layout2DSheet' = None) -> Union['Layout2DRoot', 'Layout2DSheet']:
        if value is not None:
            self.layout_2d_root.ActiveShet = value._com
            return self
        from experience.drafting_2d_interfaces import Layout2DSheet
        return Layout2DSheet(self.layout_2d_root.ActiveSheet)
    
    def layout_services(self) -> 'Layout2DServices':
        from experience.drafting_2d_interfaces.layout_2d_services import Layout2DServices
        return self.get_item("CATLayout2DServices", Layout2DServices)
    
    def parameters(self) -> 'Parameters':
        from experience.knowledge_interfaces.parameters import Parameters
        return Parameters(self.layout_2d_root.Parameters)
    
    def relations(self) -> 'Relations':
        from experience.knowledge_interfaces.relations import Relations
        return Relations(self.layout_2d_root.Relations)
    
    def rendering_mode(self, value: CatRenderingMode = None) -> Union['Layout2DRoot', CatRenderingMode]:
        if value is not None:
            self.layout_2d_root.RenderingMode = int(value)
            return self
        return CatRenderingMode.item(self.layout_2d_root.RenderingMode)  
    
    def sheets(self) -> 'Layout2DSheets':
        from experience.drafting_2d_interfaces import Layout2DSheets
        return Layout2DSheets(self.layout_2d_root.Sheets)
    
    def standard(self, value: str = None) -> Union['Layout2DRoot', str]:
        if value is not None:
            self.layout_2d_root.Standard = value
            return self
        return self.layout_2d_root.Standard
    
    def visu_in_3d(self, value: 'CatRenderingMode'= None) -> Union['Layout2DRoot', 'CatVisuIn3DMode']:
        if value is not None:
            self.layout_2d_root.VisuIn3D = int(value)
            return self
        return CatVisuIn3DMode.item(self.layout_2d_root.VisuIn3D)
    
    def reorder_sheets(self, i_ordered_sheets: list) -> 'Layout2DRoot':
        self.layout_2d_root.reorder_Sheets(i_ordered_sheets)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'