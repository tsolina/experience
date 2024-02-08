from typing import TYPE_CHECKING

from experience.mecmod_interfaces import HybridShapes, Sketches
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.mecmod_interfaces import Bodies, OrderedGeometricalSets, HybridShape

class OrderedGeometricalSet(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OrderedGeometricalSet
    """

    def __init__(self, com):
        super().__init__(com)
        self.ordered_geometrical_set = com

    def bodies(self) -> 'Bodies':
        from experience.mecmod_interfaces import Bodies
        return Bodies(self.ordered_geometrical_set.Bodies)

    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.ordered_geometrical_set.HybridShapes)

    def ordered_geometrical_sets(self) -> 'OrderedGeometricalSets':
        from experience.mecmod_interfaces import OrderedGeometricalSets
        return OrderedGeometricalSets(self.ordered_geometrical_set.OrderedGeometricalSets)

    def ordered_sketches(self) -> Sketches:
        return Sketches(self.ordered_geometrical_set.OrderedSketches)

    def insert_hybrid_shape(self, i_hybrid_shape: 'HybridShape') -> 'OrderedGeometricalSet':
        self.ordered_geometrical_set.InsertHybridShape(i_hybrid_shape._com)
        return self

    def __repr__(self):
        return f'OrderedGeometricalSet(name="{self.name}")'