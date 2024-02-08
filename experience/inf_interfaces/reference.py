from experience.system import AnyObject

class Reference(AnyObject):
    def __init__(self, com):
        super().__init__(com)
        self.reference = com

    def display_name(self) -> str:
        return self.reference.DisplayName

    def compose_with(self, i_reference: 'Reference') -> 'Reference':
        return Reference(self.reference.ComposeWith(i_reference._com))

    def __repr__(self):
        return f'Reference(name="{self.name}")'
