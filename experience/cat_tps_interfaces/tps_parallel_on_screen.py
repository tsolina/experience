from experience.system import AnyObject

class TPSParallelOnScreen(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.tps_paralel_on_screen = com


    def parallel_on_screen(self) -> bool:
        return self.tps_paralel_on_screen.ParallelOnScreen


    def zoomable(self) -> bool:
        return self.tps_paralel_on_screen.Zoomable

    def __repr__(self):
        return f'TPSParallelOnScreen(name="{self.name()}")'
