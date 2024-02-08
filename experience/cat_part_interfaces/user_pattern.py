from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import Pattern
from experience.system import AnyObject

class UserPattern(Pattern):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             PartInterfaces.Pattern
                |                                 UserPattern
    """

    def __init__(self, com):
        super().__init__(com)
        self.user_pattern = com

    def anchor_point(self, value: AnyObject = None) -> Union['UserPattern', AnyObject]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.user_pattern.AnchorPoint = value._com
            return self
        return AnyObject(self.user_pattern.AnchorPoint)

    def feature_to_locate_positions(self) -> AnyObject:
        return AnyObject(self.user_pattern.FeatureToLocatePositions)

    def add_feature_to_locate_positions(self, i_feature_to_locate_positions: AnyObject) -> 'UserPattern':
        self.user_pattern.AddFeatureToLocatePositions(i_feature_to_locate_positions._com)
        return self

    def __repr__(self):
        return f'UserPattern(name="{ self.name }")'