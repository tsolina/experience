from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces.shape import Shape

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces.sketch import Sketch

class SketchBasedShape(Shape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         SketchBasedShape
    """

    def __init__(self, com):
        super().__init__(com)
        self.sketch_based_shape = com

    def sketch(self) -> 'Sketch':
        from experience.cat_sketcher_interfaces.sketch import Sketch
        return Sketch(self.sketch_based_shape.Sketch)

    def set_profile_element(self, i_profile_element: Reference) -> 'SketchBasedShape':
        self.sketch_based_shape.SetProfileElement(i_profile_element._com)
        return self

    def __repr__(self):
        return f'SketchBasedShape(name="{self.name}")'