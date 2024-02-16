from experience.inf_interfaces import Move
from experience.mecmod_interfaces import Shape
from experience.system import AnyObject

class Solid(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         Solid
    """

    def __init__(self, com):
        super().__init__(com)
        self.solid = com

    def move(self) -> Move:
        return Move(self.solid.Move)

    # def source_element(self) -> AnyObject:
    #     return AnyObject(self.solid.SourceElement)

    # def source_product(self) -> AnyObject:
    #     return AnyObject(self.solid.SourceProduct)

    def __repr__(self):
        return f'Solid(name="{ self.name() }")'