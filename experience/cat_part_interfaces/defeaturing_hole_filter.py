from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import DefeaturingFilterWithRange

class DefeaturingHoleFilter(DefeaturingFilterWithRange):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATPartIDLItf.DefeaturingFilter
                |                         CATPartIDLItf.DefeaturingFilterWithRange
                |                             DefeaturingHoleFilter
    """

    def __init__(self, com):
        super().__init__(com)
        self.defeaturing_hole_filter = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'