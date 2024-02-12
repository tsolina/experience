from typing import TYPE_CHECKING

from experience.exceptions.exceptions import CATIAApplicationException
from experience.base_interfaces.base_application import experience_application

if TYPE_CHECKING:
    from experience.inf_interfaces import Application
    from experience.drafting_interfaces import DrawingRoot

class DrawingReady():
    def __enter__(self):
        self.app = experience_application()

        if self.app.get_workbench_id() == "":
            raise CATIAApplicationException('Editor is empty') 

        if self.app.editors().count() == 0:
            raise CATIAApplicationException('No open editors found!')           

        try:
            ed = self.app.active_editor().active_object()
        except Exception as e:
            print("exception cought")
            raise CATIAApplicationException('Editor is invalid - not geometry editor') 

        from experience.drafting_interfaces import DrawingRoot
        self.drawing = self.app.active_editor().active_object(DrawingRoot)

        if self.drawing.com_type() != "DrawingRoot":
            raise CATIAApplicationException('Drawing document is not ready')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __repr__(self):
        return 'DrawingReady'