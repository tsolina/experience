from typing import TYPE_CHECKING, Type, TypeVar, Optional, Union
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingSheet, DrawingSheets
    from experience.knowledge_interfaces import Parameters, Relations

class DrawingRoot(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingRoot
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_root = com

    def active_sheet(self) -> 'DrawingSheet':
        from experience.drafting_interfaces import DrawingSheet
        return DrawingSheet(self.drawing_root.ActiveSheet)
    
    def parameters(self) -> 'Parameters':
        from experience.knowledge_interfaces import Parameters
        return Parameters(self.drawing_root.Parameters)
    
    def relations(self) -> 'Relations':
        from experience.knowledge_interfaces import Relations
        return Relations(self.drawing_root.Relations)
    
    def sheets(self) -> 'DrawingSheets':
        from experience.drafting_interfaces import DrawingSheets
        return DrawingSheets(self.drawing_root.DrawingSheets)

    def standard(self, value: str = None) -> Union['DrawingRoot', str]:
        if value is not None:
            self.drawing_root.Standard = value
            return self
        return self.drawing_root.Standard
    
    def isolate(self) -> 'DrawingRoot':
        self.drawing_root.Isolate()
        return self

    def load_3d_data(self) -> 'DrawingRoot':
        self.drawing_root.Load3DData()
        return self

    def update(self) -> 'DrawingRoot':
        self.drawing_root.Update()
        return self
    
    def reorder_sheets(self, i_ordered_sheets: tuple) -> 'DrawingRoot':
        """ - array of sheets in new order - """
        self.drawing_root.reorder_Sheets(i_ordered_sheets)
        return self

    def __repr__(self):
        return f'DrawingRoot(name="{self.name()}")'
