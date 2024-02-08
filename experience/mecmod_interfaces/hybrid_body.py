from typing import TYPE_CHECKING

from experience.mecmod_interfaces import GeometricElements, HybridShape, HybridShapes, Sketches
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.mecmod_interfaces import HybridBodies


class HybridBody(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HybridBody   
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_body = com

    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.hybrid_body.GeometricElements)

    def hybrid_bodies(self) -> 'HybridBodies':
        from experience.mecmod_interfaces import HybridBodies
        return HybridBodies(self.hybrid_body.HybridBodies)

    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.hybrid_body.HybridShapes)

    def hybrid_sketches(self) -> Sketches:
        return Sketches(self.hybrid_body.HybridSketches)

    def append_hybrid_shape(self, i_hybrid_shape: HybridShape) -> 'HybridBody':
        self.hybrid_body.AppendHybridShape(i_hybrid_shape._com)
        return self

    def append_hybrid_shapes(self, shapes: list) -> 'HybridBody':
        for shape in shapes:
            self.append_hybrid_shape(shape)
        return self

    def __repr__(self):
        return f'HybridBody(name="{self.name}")'