from experience.system.any_object import AnyObject

class KnowledgeObject(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.knowledge_object = com

    def hidden(self, value: bool = None) -> bool:
        if value is not None:
            self.knowledge_object.Hidden = value
            return self
        return self.knowledge_object.Hidden

    def is_const(self, value: bool = None) -> bool:
        if value is not None:
            self.knowledge_object.IsConst = value
            return self
        return self.knowledge_object.IsConst

    def __repr__(self):
        return f'KnowledgeObject(name="{ self.name }")'
