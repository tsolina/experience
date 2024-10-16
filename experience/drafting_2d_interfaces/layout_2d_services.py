from experience.system import AnyObject
from .drafting_2d_types import *

class Layout2DServices(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DServices
    """

    def __init__(self, com):
        super().__init__(com)
        self.layout_2d_services = com

    def import_from_drawing(self, i_objects: list, i_option: CatImportFromDrawingOption) -> tuple:
        '''
        i_objects: array of views to copy
        returning list of drawing views
        '''
        return self.layout_2d_services.ImportFromDrawing(i_objects, int(i_option))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'

# Example  
#  Dim myPart As CATIAPart
#  Set myPart = CATIA.ActiveEditor.ActiveObject
#  Dim MyRoot As Layout2DRoot
#  Set MyRoot = myPart.GetItem("CATLayoutRoot")
#  Dim layoutServices As Layout2DServices
#  Set layoutServices = MyRoot.GetItem("CATLayout2DServices")
