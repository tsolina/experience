from experience.knowledge_interfaces.enum_param import EnumParam

class BoolParam(EnumParam):
    def __init__(self, com):
        super().__init__(com)
        self.bool_param = com

    def value(self, value: bool = None) -> bool:
        if value is not None:
            self.bool_param.Value = value
            return self
        return self.bool_param.Value

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'