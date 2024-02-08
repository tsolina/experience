from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.cat_gsm_interfaces import HybridShapeDirection
    from experience.knowledge_interfaces import Angle, Length

class HybridShapePositionTransfo(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapePositionTransfo
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_position_transfo = com

    def initial_direction_computation_mode(self, value: int = None) -> Union['HybridShapePositionTransfo', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_position_transfo.InitialDirectionComputationMode = value
            return self
        return self.hybrid_shape_position_transfo.InitialDirectionComputationMode

    def mode(self, value: int = None) -> Union['HybridShapePositionTransfo', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_position_transfo.Mode = value
            return self
        return self.hybrid_shape_position_transfo.Mode

    def profile(self, value: Reference = None) -> Union['HybridShapePositionTransfo', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_position_transfo.Profile = value._com
            return self
        return Reference(self.hybrid_shape_position_transfo.Profile)

    def get_nb_pos_angle(self) -> int:
        return self.hybrid_shape_position_transfo.GetNbPosAngle()

    def get_nb_pos_coord(self) -> int:
        return self.hybrid_shape_position_transfo.GetNbPosCoord()

    def get_pos_angle(self, i_i: int) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_position_transfo.GetPosAngle(i_i))

    def get_pos_coord(self, ii: int) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_position_transfo.GetPosCoord(ii))

    def get_pos_point(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_position_transfo.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        return self.hybrid_shape_position_transfo.GetPosSwapAxes(ii)

    def get_position_direction(self, i_i: int) -> 'HybridShapeDirection':
        from experience.cat_gsm_interfaces import HybridShapeDirection
        return HybridShapeDirection(self.hybrid_shape_position_transfo.GetPositionDirection(i_i))

    def remove_all_pos_angle(self) -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.RemoveAllPosAngle()
        return self

    def remove_all_pos_coord(self) -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.RemoveAllPosCoord()
        return self

    def set_pos_angle(self, i_i: int, i_angle: 'Angle') -> 'HybridShapePositionTransfo':
        return self.hybrid_shape_position_transfo.SetPosAngle(i_i, i_angle._com)

    def set_pos_coord(self, i_i: int, i_coordinate: 'Length') -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.SetPosCoord(i_i, i_coordinate._com)
        return self

    def set_pos_point(self, i_i: int, i_elem: Reference) -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.SetPosPoint(i_i, i_elem._com)
        return self

    def set_pos_swap_axes(self, ii: int, i_inversion: int) -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.SetPosSwapAxes(ii, i_inversion)
        return self

    def set_position_direction(self, i_i: int, i_elem: 'HybridShapeDirection') -> 'HybridShapePositionTransfo':
        self.hybrid_shape_position_transfo.SetPositionDirection(i_i, i_elem._com)
        return self

    def __repr__(self):
        return f'HybridShapePositionTransfo(name="{self.name}")'