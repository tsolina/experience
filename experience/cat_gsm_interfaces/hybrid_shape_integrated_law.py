from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class HybridShapeIntegratedLaw(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeIntegratedLaw
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_integrated_law = com

    def advanced_law(self, value: Reference = None) -> Union['HybridShapeIntegratedLaw', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_integrated_law.AdvancedLaw = value._com
            return self
        return Reference(self.hybrid_shape_integrated_law.AdvancedLaw)

    def end_param(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_integrated_law.EndParam)

    def implicit_law_interpolation_mode(self, value: int = None) -> Union['HybridShapeIntegratedLaw', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode = value
            return self
        return self.hybrid_shape_integrated_law.ImplicitLawInterpolationMode

    def invert_mapping_law(self, value: bool = None) -> Union['HybridShapeIntegratedLaw', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_integrated_law.InvertMappingLaw = value
            return self
        return self.hybrid_shape_integrated_law.InvertMappingLaw

    def pitch_law_type(self, value: int = None) -> Union['HybridShapeIntegratedLaw', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_integrated_law.PitchLawType = value
            return self
        return self.hybrid_shape_integrated_law.PitchLawType

    def spine(self, value: Reference = None) -> Union['HybridShapeIntegratedLaw', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_integrated_law.Spine = value._com
            return self
        return Reference(self.hybrid_shape_integrated_law.Spine)

    def start_param(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_integrated_law.StartParam)

    def append_new_point_and_param(self, i_point: Reference, i_param: int) -> 'HybridShapeIntegratedLaw':
        self.hybrid_shape_integrated_law.AppendNewPointAndParam(i_point._com, i_param)
        return self

    def get_point_and_param(self, i_pos: int, o_point: Reference, o_param: Reference) -> tuple:
        ### need realistic vba example to implement this function ###
        return self.hybrid_shape_integrated_law.GetPointAndParam(i_pos, o_point._com, o_param._com)

    def get_size(self) -> int:
        return self.hybrid_shape_integrated_law.GetSize()

    def remove_all_points_and_params(self) -> 'HybridShapeIntegratedLaw':
        self.hybrid_shape_integrated_law.RemoveAllPointsAndParams()
        return self

    def remove_point_and_param(self, i_point: Reference) -> 'HybridShapeIntegratedLaw':
        self.hybrid_shape_integrated_law.RemovePointAndParam(i_point._com)
        return self

    def set_end_param(self, i_end_param: int) -> 'HybridShapeIntegratedLaw':
        self.hybrid_shape_integrated_law.SetEndParam(i_end_param)
        return self

    def set_start_param(self, i_start_param: int) -> 'HybridShapeIntegratedLaw':
        self.hybrid_shape_integrated_law.SetStartParam(i_start_param)
        return self

    def __repr__(self):
        return f'HybridShapeIntegratedLaw(name="{self.name}")'