from typing import TYPE_CHECKING
from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.drafting_interfaces import DrawingGenViewProperties

class DrawingGenService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         DrawingGenService
    """

    def __init__(self, com):
        super().__init__(com)
        self.drawing_gen_service = com
    
    def drawing_gen_view_prop(self) -> 'DrawingGenViewProperties':
        from experience.drafting_interfaces import DrawingGenViewProperties
        return DrawingGenViewProperties(self.drawing_gen_service.DrawingGenViewProp)
    
    def check_view_link_integrity(self, i_info_on_view_links: list) -> bool:
        return self.drawing_gen_service.CheckViewLinkIntegrity(i_info_on_view_links)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'