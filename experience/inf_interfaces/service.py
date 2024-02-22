from experience.system import AnyObject

class Service(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.service = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'