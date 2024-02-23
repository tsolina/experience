from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces.cat_part_types import *
from experience.cat_part_interfaces import SurfaceBasedShape

if TYPE_CHECKING:
    from experience.inf_interfaces import Reference

class Partition(SurfaceBasedShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             Partition

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.partition = com_object

    def auto_mode(self, value: bool = None) -> Union['Partition', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.partition.AutoMode = value
            return self
        return self.partition.AutoMode
    
    def limit_type(self, value: CatPartitionLimitType = None) -> Union['Partition', CatPartitionLimitType]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.partition.LimitType = int(value)
            return self
        return CatPartitionLimitType.item(self.partition.LimitType)
    
    def volume(self, value: 'Reference' = None) -> Union['Partition', 'Reference']:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.partition.Volume = value._com
            return self
        from experience.inf_interfaces import Reference
        return Reference(self.partition.Volume)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'