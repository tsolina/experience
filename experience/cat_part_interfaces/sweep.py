from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.cat_part_interfaces.sketch_based_shape import SketchBasedShape

if TYPE_CHECKING:
    from experience.cat_sketcher_interfaces.sketch import Sketch

class Sweep(SketchBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             Sweep
    """

    def __init__(self, com):
        super().__init__(com)
        self.sweep = com

    def anchor_dir_reverse(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.AnchorDirReverse = value
            return self
        return self.sweep.AnchorDirReverse

    def center_curve(self) -> 'Sketch':
        from experience.cat_sketcher_interfaces.sketch import Sketch
        return Sketch(self.sweep.CenterCurve)

    def center_curve_element(self, value: Reference = None) -> Union['Sweep', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.CenterCurveElement = value._com
            return self
        return Reference(self.sweep.CenterCurveElement)

    def is_thin(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.IsThin = value
            return self
        return self.sweep.IsThin

    def merge_end(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.MergeEnd = value
            return self
        return self.sweep.MergeEnd

    def merge_mode(self, value: int = None) -> Union['Sweep', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.MergeMode = value
            return self
        return self.sweep.MergeMode

    def move_profile_to_path(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.MoveProfileToPath = value
            return self
        return self.sweep.MoveProfileToPath

    def neutral_fiber(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.NeutralFiber = value
            return self
        return self.sweep.NeutralFiber

    def normal_axis_dir_reverse(self, value: bool = None) -> Union['Sweep', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.NormalAxisDirReverse = value
            return self
        return self.sweep.NormalAxisDirReverse

    def pulling_dir_element(self, value: Reference = None) -> Union['Sweep', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.PullingDirElement = value._com
            return self
        return Reference(self.sweep.PullingDirElement)

    def reference_surface_element(self, value: Reference = None) -> Union['Sweep', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.sweep.ReferenceSurfaceElement = value._com
            return self
        return Reference(self.sweep.ReferenceSurfaceElement)

    def set_keep_angle_option(self) -> 'Sweep':
        self.sweep.SetKeepAngleOption()
        return self

    def __repr__(self):
        return f'Sweep(name="{self.name()}")'