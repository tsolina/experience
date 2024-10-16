from experience.system import AnyObject

from .layout_2d_root import Layout2DRoot

class Layout2DFactory(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DFactory
    """

    def __init__(self, com):
        super().__init__(com)
        self.layout_2d_factory = com

    def create_2d_layout(self, i_standard_name: str) -> Layout2DRoot:
        return Layout2DRoot(self.layout_2d_factory.Create2DLayout(i_standard_name))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'
    
# Dim myPart As CATIAPart
# Set myPart = CATIA.ActiveEditor.ActiveObject
# Dim MyRoot As Layout2DRoot
# Set MyRoot = myPart.GetItem("CATLayoutRoot")
# if MyRoot Is Nothing then
#    Dim MyRootFact As Layout2DFactory
#    Set MyRootFact = myPart.GetItem("CATLayoutRootFactory")
#    Set MyRoot = MyRootFact.Create2DLayout("ISO_3D")
# end if
