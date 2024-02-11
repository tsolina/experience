from experience.system.any_object import AnyObject

class Camera(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.camera = com

    def type(self) -> int:
        return self.camera.Type

    def __repr__(self):
        return f'Camera(name="{self.name()}")'
