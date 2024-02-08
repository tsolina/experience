from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces.hybrid_shape import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces.angle import Angle

class HybridShapeRotate(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeRotate
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_rotate = com

    def angle(self) -> 'Angle':
        from experience.knowledge_interfaces.angle import Angle
        return Angle(self.hybrid_shape_rotate.Angle)

    def angle_value(self, value: float = None) -> Union['HybridShapeRotate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.AngleValue = value
            return self
        return self.hybrid_shape_rotate.AngleValue

    def axis(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.Axis = value._com
            return self
        return Reference(self.hybrid_shape_rotate.Axis)

    def elem_to_rotate(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.ElemToRotate = value._com
            return self
        return Reference(self.hybrid_shape_rotate.ElemToRotate)

    def first_element(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.FirstElement = value._com
            return self
        return Reference(self.hybrid_shape_rotate.FirstElement)

    def first_point(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.FirstPoint = value._com
            return self
        return Reference(self.hybrid_shape_rotate.FirstPoint)

    def orientation_of_first_element(self, value: bool = None) -> Union['HybridShapeRotate', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.OrientationOfFirstElement = value
            return self
        return self.hybrid_shape_rotate.OrientationOfFirstElement

    def orientation_of_second_element(self, value: bool = None) -> Union['HybridShapeRotate', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.OrientationOfSecondElement = value
            return self
        return self.hybrid_shape_rotate.OrientationOfSecondElement

    def rotation_type(self, value: int = None) -> Union['HybridShapeRotate', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.RotationType = value
            return self
        return self.hybrid_shape_rotate.RotationType

    def second_element(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.SecondElement = value._com
            return self
        return Reference(self.hybrid_shape_rotate.SecondElement)

    def second_point(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.SecondPoint = value._com
            return self
        return Reference(self.hybrid_shape_rotate.SecondPoint)

    def third_point(self, value: Reference = None) -> Union['HybridShapeRotate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.ThirdPoint = value._com
            return self
        return Reference(self.hybrid_shape_rotate.ThirdPoint)

    def volume_result(self, value: bool = None) -> Union['HybridShapeRotate', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_rotate.VolumeResult = value
            return self
        return self.hybrid_shape_rotate.VolumeResult

    def get_creation_mode(self) -> int:
        return self.hybrid_shape_rotate.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> 'HybridShapeRotate':
        self.hybrid_shape_rotate.SetCreationMode(i_creation)
        return self

    def __repr__(self):
        return f'HybridShapeRotate(name="{self.name}")'