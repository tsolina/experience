from experience.knowledge_interfaces.knowledge_object import KnowledgeObject

class KnowledgeActivateObject(KnowledgeObject):
    def __init__(self, com):
        super().__init__(com)
        self.knowledge_activate_object = com

    def activated(self) -> bool:
        return self.knowledge_activate_object.Activated

    def activate(self) -> 'KnowledgeActivateObject':
        self.knowledge_activate_object.Activate()
        return self

    def deactivate(self) -> 'KnowledgeActivateObject':
        self.knowledge_activate_object.Deactivate()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'