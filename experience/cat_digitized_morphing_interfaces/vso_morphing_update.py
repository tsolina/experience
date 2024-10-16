from experience.system import AnyObject

class VSOMorphingUpdate(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSOMorphingUpdate
    """

    def __init__(self, com):
        super().__init__(com)
        self.vso_morphing_update = com

    def update_input_file(self, i_new_file_path: str) -> 'VSOMorphingUpdate':
        self.vso_morphing_update.UpdateInputFile(i_new_file_path)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'