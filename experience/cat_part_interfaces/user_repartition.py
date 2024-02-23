from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.repartition import Repartition
from experience.system import AnyObject

class UserRepartition(Repartition):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATPartIDLItf.Repartition
                |                         UserRepartition
    """

    def __init__(self, com):
        super().__init__(com)
        self.user_repartition = com

    def feature_to_locate_positions(self, value: AnyObject = None) -> Union['UserRepartition', AnyObject]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.user_repartition.FeatureToLocatePositions = value._com
            return self
        return AnyObject(self.user_repartition.FeatureToLocatePositions)

    def add_feature_to_locate_positions(self, i_feature_to_locate_positions: AnyObject) -> 'UserRepartition':
        self.user_repartition.AddFeatureToLocatePositions(i_feature_to_locate_positions._com)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'