from experience.system.any_object import AnyObject

class Service(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.service = com

    def __repr__(self):
        return f'Service(name="{self.name}")'
