from typing import TYPE_CHECKING

from experience.exceptions.exceptions import CATIAApplicationException
from experience.base_interfaces.base_application import experience_application

if TYPE_CHECKING:
    from experience.inf_interfaces import Application
    from experience.mecmod_interfaces import Part

class PartReady():
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

        from experience.mecmod_interfaces import Part
        self.part = self.app.active_editor().active_object(Part)

        if self.part.com_type() != "Part":
            raise CATIAApplicationException('Part document is not ready')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __repr__(self):
        return 'PartReady'