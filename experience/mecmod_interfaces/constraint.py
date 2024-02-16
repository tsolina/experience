from typing import Union
from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import Dimension
from experience.system import AnyObject

class Constraint(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Constraint
    """

    def __init__(self, com):
        super().__init__(com)
        self.constraint = com

    def angle_sector(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.AngleSector = value
            return self        
        return self.constraint.AngleSector

    def dimension(self) -> Dimension:
        return Dimension(self.constraint.Dimension)

    def distance_config(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.DistanceConfig = value
            return self    
        return self.constraint.DistanceConfig

    def distance_direction(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.DistanceDirection = value
            return self    
        return self.constraint.DistanceDirection

    def mode(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Mode = value
            return self   
        return self.constraint.Mode

    def orientation(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Orientation = value
            return self   
        return self.constraint.Orientation

    def reference_axis(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.ReferenceAxis = value
            return self
        return self.constraint.ReferenceAxis

    def reference_type(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.ReferenceType = value
            return self
        return self.constraint.ReferenceType

    def side(self, value: int = None) -> Union['Constraint', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Side = value
            return self
        return self.constraint.Side

    def status(self) -> int:
        return self.constraint.Status

    def type(self) -> int:
        return self.constraint.Type

    def activate(self) -> 'Constraint':
        self.constraint.Activate()
        return self

    def deactivate(self) -> 'Constraint':
        self.constraint.Deactivate()
        return self

    def get_constraint_element(self, i_element_number: int) -> Reference:
        return Reference(self.constraint.GetConstraintElement(i_element_number))

    def get_constraint_visu_location(self, o_anchor_point: tuple, o_anchor_vector: tuple) -> tuple:
        return self.constraint.GetConstraintVisuLocation(o_anchor_point, o_anchor_vector)

    def is_inactive(self) -> bool:
        return self.constraint.IsInactive()

    def set_constraint_element(self, i_element_number: int, i_new_element: Reference) -> 'Constraint':
        self.constraint.SetConstraintElement(i_element_number, i_new_element._com)
        return self

    def set_constraint_visu_location(self, i_new_x: float, i_new_y: float, i_new_z: float) -> 'Constraint':
        self.constraint.SetConstraintVisuLocation(i_new_x, i_new_y, i_new_z)
        return self

    def __repr__(self):
        return f'Constraint(name="{self.name()}")'