from experience.system import AnyObject

class SemanticGDTFrameExtension(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTFrameExtension
    """

    def __init__(self, com):
        super().__init__(com)
        self.semantic_gdt_frame_extension = com

    def direction_specification(self) -> str:
        return self.semantic_gdt_frame_extension.DirectionSpecification

    def type(self) -> str:
        return self.semantic_gdt_frame_extension.Type

    def direction_reference(self) -> str:
        return self.semantic_gdt_frame_extension.DirectionReference()

    def orientation(self) -> float:
        return self.semantic_gdt_frame_extension.Orientation()