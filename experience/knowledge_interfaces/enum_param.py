from experience.knowledge_interfaces.parameter import Parameter

class EnumParam(Parameter):
    def __init__(self, com):
        super().__init__(com)
        self.enum_param = com

    def value_enum(self, value: str = None) -> str:
        if value is not None:
            self.enum_param.ValueEnum = value
            return self
        return self.enum_param.ValueEnum

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'