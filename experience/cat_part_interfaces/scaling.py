from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import RealParam

class Scaling(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Scaling
    """

    def __init__(self, com):
        super().__init__(com)
        self.scaling = com

    def factor(self) -> 'RealParam':
        from experience.knowledge_interfaces import RealParam
        return RealParam(self.scaling.Factor)

    def scaling_reference(self, value: Reference = None) -> Union['Scaling', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.scaling.ScalingReference = value._com
            return self
        return Reference(self.scaling.ScalingReference)

    def __repr__(self):
        return f'Scaling(name="{ self.name() }")'