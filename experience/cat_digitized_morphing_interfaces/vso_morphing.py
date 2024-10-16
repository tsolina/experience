from experience.system import AnyObject

class VSOMorphing(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSOMorphing
    """

    def __init__(self, com):
        super().__init__(com)
        self.vso_morphing = com

    def add_vector_field(self, i_vector_field: AnyObject, i_scale:float, i_copy_vector_field_as_result: bool) -> 'VSOMorphing':
        self.vso_morphing.AddVectorField(i_vector_field._com, i_scale, i_copy_vector_field_as_result)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'