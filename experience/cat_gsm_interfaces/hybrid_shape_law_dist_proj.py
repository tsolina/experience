from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeLawDistProj(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeLawDistProj
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_law_dist_proj = com

    def applied_unit_symbol(self, i_symbol: str) -> 'HybridShapeLawDistProj':
        self.hybrid_shape_law_dist_proj.AppliedUnitSymbol = i_symbol
        return self

    def definition(self, value: Reference = None) -> Union['HybridShapeLawDistProj', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_law_dist_proj.Definition = value._com
            return self
        return Reference(self.hybrid_shape_law_dist_proj.Definition)

    def measure_unit_symbol(self, value: str) -> 'HybridShapeLawDistProj':
        self.hybrid_shape_law_dist_proj.MeasureUnitSymbol = value
        return self

    def parameter_on_definition(self, value: bool = None) -> Union['HybridShapeLawDistProj', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_law_dist_proj.ParameterOnDefinition = value
            return self
        return self.hybrid_shape_law_dist_proj.ParameterOnDefinition

    def positive_direction_orientation(self, value: int = None) -> Union['HybridShapeLawDistProj', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation = value
            return self
        return self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation

    def reference(self, value: Reference = None) -> Union['HybridShapeLawDistProj', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_law_dist_proj.Reference = value._com
            return self
        return Reference(self.hybrid_shape_law_dist_proj.Reference)

    def scaling(self, value: float = None) -> Union['HybridShapeLawDistProj', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_law_dist_proj.Scaling = value
            return self
        return self.hybrid_shape_law_dist_proj.Scaling

    def get_applied_unit_symbol(self) -> str:
        return self.hybrid_shape_law_dist_proj.GetAppliedUnitSymbol()

    def get_measure_unit_symbol(self) -> str:
        return self.hybrid_shape_law_dist_proj.GetMeasureUnitSymbol()

    def get_plane_normal(self, o_normal: tuple) -> tuple:
        ### to test if this works as expected ###
        return self._get_safe_array(self._com, "GetPlaneNormal", 2)
        # return self.hybrid_shape_law_dist_proj.GetPlaneNormal(o_normal)

    def is_heterogeneous_law(self) -> bool:
        return self.hybrid_shape_law_dist_proj.IsHeterogeneousLaw()

    def put_plane_normal(self, i_normal: tuple) -> 'HybridShapeLawDistProj':
        self.hybrid_shape_law_dist_proj.PutPlaneNormal(i_normal)
        return self

    def __repr__(self):
        return f'HybridShapeLawDistProj(name="{self.name}")'