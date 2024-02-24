from experience.mecmod_interfaces import HybridBodies, HybridShape, HybridShapes, OrderedGeometricalSets, Shapes, Sketches
from experience.system import AnyObject

class Body(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Body
    """

    def __init__(self, com):
        super().__init__(com)
        self.body = com

    def hybrid_bodies(self) -> HybridBodies:
        return HybridBodies(self.body.HybridBodies)

    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.body.HybridShapes)

    def in_boolean_operation(self) -> bool:
        return self.body.InBooleanOperation

    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        return OrderedGeometricalSets(self.body.OrderedGeometricalSets)

    def shapes(self) -> Shapes:
        return Shapes(self.body.Shapes)

    def sketches(self) -> Sketches:
        return Sketches(self.body.Sketches)

    def insert_hybrid_shape(self, i_hybrid_shape: HybridShape) -> 'Body':
        self.body.InsertHybridShape(i_hybrid_shape._com)
        return self