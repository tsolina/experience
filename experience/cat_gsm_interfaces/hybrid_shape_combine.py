from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeCombine(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCombine
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_combine = com

    def direction1(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCombine', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.Direction1 = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_combine.Direction1)

    def direction2(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeCombine', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.Direction2 = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_combine.Direction2)

    def elem1(self, value: Reference = None) -> Union['HybridShapeCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.Elem1 = value._com
            return self
        return Reference(self.hybrid_shape_combine.Elem1)

    def elem2(self, value: Reference = None) -> Union['HybridShapeCombine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.Elem2 = value._com
            return self
        return Reference(self.hybrid_shape_combine.Elem2)

    def nearest_solution(self, value: int = None) -> Union['HybridShapeCombine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.NearestSolution = value
            return self
        return self.hybrid_shape_combine.NearestSolution

    def solution_type_combine(self, value: int = None) -> Union['HybridShapeCombine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_combine.SolutionTypeCombine = value
            return self
        return self.hybrid_shape_combine.SolutionTypeCombine

    def __repr__(self):
        return f'HybridShapeCombine(name="{self.name}")'