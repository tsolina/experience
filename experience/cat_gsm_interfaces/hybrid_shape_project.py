from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeProject(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeProject
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_project = com

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeProject', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_project.Direction)

    def elem_to_project(self, value: Reference = None) -> Union['HybridShapeProject', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.ElemToProject = value._com
            return self
        return Reference(self.hybrid_shape_project.ElemToProject)

    def extrapolation_mode(self, value: int = None) -> Union['HybridShapeProject', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.ExtrapolationMode = value
            return self
        return self.hybrid_shape_project.ExtrapolationMode

    def maximum_deviation_value(self, value: float = None) -> Union['HybridShapeProject', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.MaximumDeviationValue = value
            return self
        return self.hybrid_shape_project.MaximumDeviationValue

    def normal(self, value: bool = None) -> Union['HybridShapeProject', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.Normal = value
            return self
        return self.hybrid_shape_project.Normal

    def smoothing_type(self, value: int = None) -> Union['HybridShapeProject', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.SmoothingType = value
            return self
        return self.hybrid_shape_project.SmoothingType

    def solution_type(self, value: int = None) -> Union['HybridShapeProject', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.SolutionType = value
            return self
        return self.hybrid_shape_project.SolutionType

    def support(self, value: Reference = None) -> Union['HybridShapeProject', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.Support = value._com
            return self
        return Reference(self.hybrid_shape_project.Support)

    def p_3d_smoothing(self, value: bool = None) -> Union['HybridShapeProject', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_project.p3DSmoothing = value
            return self
        return self.hybrid_shape_project.p3DSmoothing

    def __repr__(self):
        return f'HybridShapeProject(name="{self.name}")'