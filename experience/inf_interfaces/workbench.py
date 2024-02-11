from experience.system import AnyObject

class Workbench(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.workbench = com

    def __repr__(self):
        return f'Workbench(name="{self.name()}")'