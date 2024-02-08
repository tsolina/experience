from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.cat_part_interfaces import TransformationShape
from experience.system import AnyObject

class Mirror(TransformationShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             Mirror
    """

    def __init__(self, com):
        super().__init__(com)
        self.mirror = com

    def desing_intent(self, value: float = None) -> Union['Mirror', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.mirror.DesignIntent = value
            return self
        return self.mirror.DesignIntent

    def mirroring_object(self) -> AnyObject:
        return AnyObject(self.mirror.MirroringObject)

    def mirroring_plane(self, value: Reference = None) -> Union['Mirror', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.mirror.MirroringPlane = value._com
            return self
        return Reference(self.mirror.MirroringPlane)

    def __repr__(self):
        return f'Mirror(name="{ self.name }")'