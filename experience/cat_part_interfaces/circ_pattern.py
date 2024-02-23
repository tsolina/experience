from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import Pattern

if TYPE_CHECKING:
    from experience.knowledge_interfaces import IntParam
    from experience.cat_part_interfaces import AngularRepartition, LinearRepartition

class CircPattern(Pattern):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             PartInterfaces.Pattern
                |                                 CircPattern
    """

    def __init__(self, com):
        super().__init__(com)
        self.circ_pattern = com

    def angular_direction_row(self) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.circ_pattern.AngularDirectionRow)

    def angular_repartition(self) -> 'AngularRepartition':
        from experience.cat_part_interfaces import AngularRepartition
        return AngularRepartition(self.circ_pattern.AngularRepartition)

    def circular_pattern_parameters(self, value: CatCircularPatternParameters = None) -> Union['CircPattern', CatCircularPatternParameters]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.circ_pattern.CircularPatternParameters = int(value)
            return self
        return CatCircularPatternParameters.item(self.circ_pattern.CircularPatternParameters)

    def radial_alignment(self, value: bool = None) -> Union['CircPattern', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.circ_pattern.RadialAlignment = value
            return self
        return self.circ_pattern.RadialAlignment

    def radial_direction_row(self) -> 'IntParam':
        from experience.knowledge_interfaces import IntParam
        return IntParam(self.circ_pattern.RadialDirectionRow)

    def radial_repartition(self) -> 'LinearRepartition':
        from experience.cat_part_interfaces import LinearRepartition
        return LinearRepartition(self.circ_pattern.RadialRepartition)

    def rotation_orientation(self, value: bool = None) -> Union['CircPattern', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.circ_pattern.RotationOrientation = value
            return self
        return self.circ_pattern.RotationOrientation

    def get_rotation_axis(self, io_rotation_axis: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetRotationAxis", 2)

    def get_rotation_center(self, io_rotation_center: tuple) -> tuple[float, float, float]:
        return self._get_safe_array(self._com, "GetRotationCenter", 2)

    def set_instance_angular_spacing(self, i_instance_number: int, i_angular_spacing: float) -> 'CircPattern':
        self.circ_pattern.SetInstanceAngularSpacing(i_instance_number, i_angular_spacing)
        return self

    def set_rotation_axis(self, i_rotation_axis: Reference) -> 'CircPattern':
        self.circ_pattern.SetRotationAxis(i_rotation_axis._com)
        return self

    def set_rotation_center(self, i_rotation_center: Reference) -> 'CircPattern':
        self.circ_pattern.SetRotationCenter(i_rotation_center._com)
        return self

    def set_unequal_instance_number(self, i_instance_number: int) -> 'CircPattern':
        self.circ_pattern.SetUnequalInstanceNumber(i_instance_number)
        return self

    def set_unequal_step(self, i_instance_number: int) -> 'CircPattern':
        self.circ_pattern.SetUnequalStep(i_instance_number)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'