from typing import Union
from experience.inf_interfaces import Reference
from experience.knowledge_interfaces import Dimension
from experience.system import AnyObject
from experience.mecmod_interfaces.mecmod_types import *

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

    def angle_sector(self, value: CatConstraintAngleSector = None) -> Union['Constraint', CatConstraintAngleSector]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.AngleSector = int(value)
            return self        
        return CatConstraintAngleSector.item(self.constraint.AngleSector)

    def dimension(self) -> Dimension:
        return Dimension(self.constraint.Dimension)

    def distance_config(self, value: CatConstraintDistConfig = None) -> Union['Constraint', CatConstraintDistConfig]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.DistanceConfig = int(value)
            return self    
        return CatConstraintDistConfig.item(self.constraint.DistanceConfig)

    def distance_direction(self, value: CatConstraintDistDirection = None) -> Union['Constraint', CatConstraintDistDirection]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.DistanceDirection = int(value)
            return self    
        return CatConstraintDistDirection.item(self.constraint.DistanceDirection)

    def mode(self, value: CatConstraintMode = None) -> Union['Constraint', CatConstraintMode]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Mode = int(value)
            return self   
        return CatConstraintMode.item(self.constraint.Mode)

    def orientation(self, value: CatConstraintOrientation = None) -> Union['Constraint', CatConstraintOrientation]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Orientation = int(value)
            return self   
        return CatConstraintOrientation.item(self.constraint.Orientation)

    def reference_axis(self, value: CatConstraintRefAxis = None) -> Union['Constraint', CatConstraintRefAxis]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.ReferenceAxis = int(value)
            return self
        return CatConstraintRefAxis.item(self.constraint.ReferenceAxis)

    def reference_type(self, value: CatConstraintRefType = None) -> Union['Constraint', CatConstraintRefType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.ReferenceType = int(value)
            return self
        return CatConstraintRefType.item(self.constraint.ReferenceType)

    def side(self, value: CatConstraintSide = None) -> Union['Constraint', CatConstraintSide]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.constraint.Side = int(value)
            return self
        return CatConstraintSide.item(self.constraint.Side)

    def status(self) -> CatConstraintStatus:
        return CatConstraintStatus.item(self.constraint.Status)

    def type(self) -> CatConstraintType:
        return CatConstraintType.item(self.constraint.Type)

    def activate(self) -> 'Constraint':
        self.constraint.Activate()
        return self

    def deactivate(self) -> 'Constraint':
        self.constraint.Deactivate()
        return self

    def get_constraint_element(self, i_element_number: int) -> Reference:
        return Reference(self.constraint.GetConstraintElement(i_element_number))

    def get_constraint_visu_location(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        return self._get_safe_array_multi(self.constraint, "GetConstraintVisuLocation", (2, 2))

    def is_inactive(self) -> bool:
        return self.constraint.IsInactive()

    def set_constraint_element(self, i_element_number: int, i_new_element: Reference) -> 'Constraint':
        self.constraint.SetConstraintElement(i_element_number, i_new_element._com)
        return self

    def set_constraint_visu_location(self, i_new_x: float, i_new_y: float, i_new_z: float) -> 'Constraint':
        self.constraint.SetConstraintVisuLocation(i_new_x, i_new_y, i_new_z)
        return self