from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces.reference import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length, RealParam

class HybridShapeHelix(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeHelix
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_helix = com

    def axis(self, value: Reference = None) -> Union['HybridShapeHelix', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.Axis = value._com
            return self
        return Reference(self.hybrid_shape_helix.Axis)

    def clockwise_revolution(self, value: bool = None) -> Union['HybridShapeHelix', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.ClockwiseRevolution = value
            return self
        return self.hybrid_shape_helix.ClockwiseRevolution

    def height(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_helix.Height)

    def invert_axis(self, value: bool = None) -> Union['HybridShapeHelix', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.InvertAxis = value
            return self
        return self.hybrid_shape_helix.InvertAxis

    def pitch(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_helix.Pitch)

    def pitch2(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_helix.Pitch2)

    def pitch_law_type(self, value: int = None) -> Union['HybridShapeHelix', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.PitchLawType = value
            return self
        return self.hybrid_shape_helix.PitchLawType

    def profile(self, value: Reference = None) -> Union['HybridShapeHelix', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.Profile = value._com
            return self
        return Reference(self.hybrid_shape_helix.Profile)

    def revol_number(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.hybrid_shape_helix.RevolNumber)

    def starting_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_helix.StartingAngle)

    def starting_point(self, value: Reference = None) -> Union['HybridShapeHelix', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.StartingPoint = value._com
            return self
        return Reference(self.hybrid_shape_helix.StartingPoint)

    def taper_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_helix.TaperAngle)

    def taper_outward(self, value: bool = None) -> Union['HybridShapeHelix', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_helix.TaperOutward = value
            return self
        return self.hybrid_shape_helix.TaperOutward

    def set_height(self, i_height: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetHeight(i_height)
        return self

    def set_pitch(self, i_pitch: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetPitch(i_pitch)
        return self

    def set_pitch2(self, i_pitch2: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetPitch2(i_pitch2)
        return self

    def set_revolution_number(self, i_nb_revol: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetRevolutionNumber(i_nb_revol)
        return self

    def set_starting_angle(self, i_starting_angle: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetStartingAngle(i_starting_angle)
        return self

    def set_taper_angle(self, i_taper_angle: float) -> 'HybridShapeHelix':
        self.hybrid_shape_helix.SetTaperAngle(i_taper_angle)
        return self

    def __repr__(self):
        return f'HybridShapeHelix(name="{ self.name }")'