from experience.mecmod_interfaces import Shape

class TransformationShape(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         TransformationShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.transformation_shape = com

    def __repr__(self):
        return f'TransformationShape(name="{ self.name }")'