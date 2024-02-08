from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Length

class HybridShapeTranslate(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeTranslate
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_translate = com

    def coord_x_value(self, value: float = None) -> Union['HybridShapeTranslate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.CoordXValue = value
            return self
        return self.hybrid_shape_translate.CoordXValue

    def coord_y_value(self, value: float = None) -> Union['HybridShapeTranslate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.CoordYValue = value
            return self
        return self.hybrid_shape_translate.CoordYValue

    def coord_z_value(self, value: float = None) -> Union['HybridShapeTranslate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.CoordZValue = value
            return self
        return self.hybrid_shape_translate.CoordZValue

    def direction(self, value: 'HybridShapeDirection' = None) -> Union['HybridShapeTranslate', 'HybridShapeDirection']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.Direction = value._com
            return self
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_translate.Direction)

    def distance(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_translate.Distance)

    def distance_value(self, value: float = None) -> Union['HybridShapeTranslate', float]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.DistanceValue = value
            return self
        return self.hybrid_shape_translate.DistanceValue

    def elem_to_translate(self, value: Reference = None) -> Union['HybridShapeTranslate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.ElemToTranslate = value._com
            return self
        return Reference(self.hybrid_shape_translate.ElemToTranslate)

    def first_point(self, value: Reference = None) -> Union['HybridShapeTranslate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.FirstPoint = value._com
            return self
        return Reference(self.hybrid_shape_translate.FirstPoint)

    def ref_axis_system(self, value: Reference = None) -> Union['HybridShapeTranslate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.RefAxisSystem = value._com
            return self
        return Reference(self.hybrid_shape_translate.RefAxisSystem)

    def second_point(self, value: Reference = None) -> Union['HybridShapeTranslate', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.SecondPoint = value._com
            return self
        return Reference(self.hybrid_shape_translate.SecondPoint)

    def vector_type(self, value: int = None) -> Union['HybridShapeTranslate', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.VectorType = value
            return self
        return self.hybrid_shape_translate.VectorType

    def volume_result(self, value: bool = None) -> Union['HybridShapeTranslate', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_translate.VolumeResult = value
            return self
        return self.hybrid_shape_translate.VolumeResult

    def get_creation_mode(self) -> int:
        return self.hybrid_shape_translate.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> 'HybridShapeTranslate':
        self.hybrid_shape_translate.SetCreationMode(i_creation)
        return self

    def __repr__(self):
        return f'HybridShapeTranslate(name="{self.name}")'