from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import Repartition

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle

class AngularRepartition(Repartition):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartInterfaces.Repartition
                |                         AngularRepartition
    """

    def __init__(self, com):
        super().__init__(com)
        self.angular_repartition = com

    def angular_spacing(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.angular_repartition.AngularSpacing)

    def instance_spacing(self) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.angular_repartition.InstanceSpacing)

    def __repr__(self):
        return f'AngularRepartition(name="{ self.name }")'