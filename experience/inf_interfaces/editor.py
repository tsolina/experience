from typing import TYPE_CHECKING, Type, TypeVar, Optional
from experience.system import AnyObject

T = TypeVar('T', bound=AnyObject)

if TYPE_CHECKING:
    from experience.inf_interfaces import Selection, Service, EditorServices

class Editor(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Editor
    """

    def __init__(self, com):
        super().__init__(com)
        self.editor = com


    def active_object(self, value: Optional[Type[T]] = None) -> T:
        if value is not None:
            return value(self.editor.ActiveObject)
        return AnyObject(self.editor.ActiveObject)

    def selection(self) -> 'Selection':
        from experience.inf_interfaces import Selection
        return Selection(self.editor.Selection)

    def get_service(self, i_service: str) -> 'Service':
        from experience.inf_interfaces import Service
        return Service(self.editor.GetService(i_service))
    
    def services(self) -> 'EditorServices':
        from experience.inf_interfaces import EditorServices
        return EditorServices(self.editor) 

    def __repr__(self):
        return f'Editor(name="{self.name()}")'
