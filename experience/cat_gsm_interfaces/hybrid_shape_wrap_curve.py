from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection

class HybridShapeWrapCurve(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeWrapCurve
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_wrap_curve = com

    def first_curves_constraint(self, value: int = None) -> Union['HybridShapeWrapCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_curve.FirstCurvesConstraint = value
            return self
        return self.hybrid_shape_wrap_curve.FirstCurvesConstraint

    def last_curves_constraint(self, value: int = None) -> Union['HybridShapeWrapCurve', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_curve.LastCurvesConstraint = value
            return self
        return self.hybrid_shape_wrap_curve.LastCurvesConstraint

    def surface(self, value: Reference = None) -> Union['HybridShapeWrapCurve', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_wrap_curve.Surface = value._com
            return self
        return Reference(self.hybrid_shape_wrap_curve.Surface)

    def get_curves(self, i_position: int) -> tuple[Reference, Reference]:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeWrapCurve","GetCurves"), ("Reference", "Reference"))

    def get_number_of_curves(self) -> int:
        return self.hybrid_shape_wrap_curve.GetNumberOfCurves()

    def get_reference_direction(self, o_direction_type: int, o_direction: 'HybridShapeDirection') -> tuple[int, 'HybridShapeDirection']:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeWrapCurve","GetReferenceDirection"), ("Long", "HybridShapeDirection"))       

    def get_reference_spine(self) -> tuple[int, 'Reference']:
        ### need working vba example to tune this function ###
        return self._get_multi([self._com], ("HybridShapeWrapCurve","GetReferenceSpine"), ("Long", "Reference"))  

    def insert_curves(self, i_position: int, i_reference_curve: Reference, i_target_curve: Reference) -> 'HybridShapeWrapCurve':
        self.hybrid_shape_wrap_curve.InsertCurves(i_position, i_reference_curve._com, i_target_curve._com)
        return self

    def insert_reference_curve(self, i_position: int, i_reference_curve: Reference) -> 'HybridShapeWrapCurve':
        self.hybrid_shape_wrap_curve.InsertReferenceCurve(i_position, i_reference_curve._com)
        return self

    def remove_curves(self, i_position: int) -> 'HybridShapeWrapCurve':
        self.hybrid_shape_wrap_curve.RemoveCurves(i_position)
        return self

    def set_reference_direction(self, i_direction: 'HybridShapeDirection') -> 'HybridShapeWrapCurve':
        self.hybrid_shape_wrap_curve.SetReferenceDirection(i_direction._com)
        return self

    def set_reference_spine(self, i_spine: Reference) -> 'HybridShapeWrapCurve':
        self.hybrid_shape_wrap_curve.SetReferenceSpine(i_spine._com)
        return self

    def __repr__(self):
        return f'HybridShapeWrapCurve(name="{self.name}")'