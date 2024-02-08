from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class HybridShapeHealing(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeHealing
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_healing = com

    def canonic_free_mode(self, value: int = None) -> Union['HybridShapeHealing', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_healing.CononicFreeMode = value
            return self
        return self.hybrid_shape_healing.CononicFreeMode

    def continuity(self, value: int = None) -> Union['HybridShapeHealing', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_healing.Continuity = value
            return self
        return self.hybrid_shape_healing.Continuity

    def distance_objective(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_healing.DistanceObjective)

    def merging_distance(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_healing.MergingDistance)

    def no_of_bodies_to_heal(self) -> int:
        return self.hybrid_shape_healing.NoOfBodiesToHeal

    def no_of_edges_to_keep_sharp(self) -> int:
        return self.hybrid_shape_healing.NoOfEdgesToKeepSharp

    def no_of_elements_to_freeze(self) -> int:
        return self.hybrid_shape_healing.NoOfElementsToFreeze

    def sharpness_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_healing.SharpnessAngle)

    def tangency_angle(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.hybrid_shape_healing.TangencyAngle)

    def tangency_objective(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.hybrid_shape_healing.TangencyObjective)

    def add_body_to_heal(self, i_body: Reference) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.AddBodyToHeal(i_body._com)
        return self

    def add_edge_to_keep_sharp(self, i_edge: Reference) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.AddEdgeToKeepSharp(i_edge._com)
        return self

    def add_elements_to_freeze(self, i_element: Reference) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.AddElementsToFreeze(i_element._com)
        return self

    def get_body_to_heal(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetBodyToHeal(i_position))

    def get_edge_to_keep_sharp(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetEdgeToKeepSharp(i_position))

    def get_element_to_freeze(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetElementToFreeze(i_position))

    def remove_body_to_heal(self, i_position: int) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.RemoveBodyToHeal(i_position)
        return self

    def remove_edge_to_keep_sharp(self, i_position: int) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.RemoveEdgeToKeepSharp(i_position)
        return self

    def remove_element_to_freeze(self, i_position: int) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.RemoveElementToFreeze(i_position)
        return self

    def replace_to_heal_element(self, i_index: int, i_new_heal: Reference) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.ReplaceToHealElement(i_index, i_new_heal._com)
        return self

    def set_distance_objective(self, i_distance_objective: float) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.SetDistanceObjective(i_distance_objective)
        return self

    def set_merging_distance(self, i_merging_distance: float) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.SetMergingDistance(i_merging_distance)
        return self

    def set_sharpness_angle(self, i_sharpness_angle: float) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.SetSharpnessAngle(i_sharpness_angle)
        return self

    def set_tangency_angle(self, i_tangency_angle: float) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.SetTangencyAngle(i_tangency_angle)
        return self

    def set_tangency_objective(self, i_tangency_objective: float) -> 'HybridShapeHealing':
        self.hybrid_shape_healing.SetTangencyObjective(i_tangency_objective)
        return self

    def __repr__(self):
        return f'HybridShapeHealing(name="{ self.name }")'