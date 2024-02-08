from experience.cat_tps_interfaces import Capture
from experience.mecmod_interfaces import Factory

class CaptureFactory(Factory):
    def __init__(self, com):
        super().__init__(com)
        self.capture_factory = com

    def create_capture(self) -> Capture:
        return Capture(self.capture_factory.CreateCapture())

    def __repr__(self):
        return f'CaptureFactory(name="{self.name}")'
