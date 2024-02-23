from typing import Union, Optional, TYPE_CHECKING

from experience.cat_part_interfaces import DefeaturingFilter

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle, Length

class DefeaturingFilterWithRange(DefeaturingFilter):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATPartIDLItf.DefeaturingFilter
                |                         DefeaturingFilterWithRange
    """

    def __init__(self, com):
        super().__init__(com)
        self.defeaturing_filter_with_range = com

    def get_maximum_activity(self, i_range_id: str) -> bool:
        return self.defeaturing_filter_with_range.getMaximumActivity(i_range_id)

    def get_maximum_angle(self, i_range_id: str) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.defeaturing_filter_with_range.getMaximumAngle(i_range_id))

    def get_maximum_length(self, i_range_id: str) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.defeaturing_filter_with_range.getMaximumLength(i_range_id))

    def get_maximum_value(self, i_range_id: str) -> float:
        return self.defeaturing_filter_with_range.getMaximumValue(i_range_id)
    
    def get_minimum_activity(self, i_range_id: str) -> bool:
        return self.defeaturing_filter_with_range.getMinimumActivity(i_range_id)

    def get_minumum_angle(self, i_range_id: str) -> 'Angle':
        from experience.knowledge_interfaces import Angle
        return Angle(self.defeaturing_filter_with_range.getMinimumAngle(i_range_id))
    
    def get_minimum_length(self, i_range_id: str) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.defeaturing_filter_with_range.getMinimumLength(i_range_id))  

    def get_minimum_value(self, i_range_id: str) -> float:
        return self.defeaturing_filter_with_range.getMinimumLength(i_range_id)
    
    def set_maximum_activity(self, i_range_id: str, i_value: bool) -> 'DefeaturingFilterWithRange':
        self.defeaturing_filter_with_range.setMaximumActivity(i_range_id, i_value)
        return self
    
    def set_maximum_value(self, i_range_id: str, i_value: bool) -> 'DefeaturingFilterWithRange':
        self.defeaturing_filter_with_range.setMaximumValue(i_range_id, i_value)
        return self
    
    def set_minimum_activity(self, i_range_id: str, i_value: bool) -> 'DefeaturingFilterWithRange':
        self.defeaturing_filter_with_range.setMinimumActivity(i_range_id, i_value)
        return self
    
    def set_minimum_value(self, i_range_id: str, i_value: bool) -> 'DefeaturingFilterWithRange':
        self.defeaturing_filter_with_range.setMinimumValue(i_range_id, i_value)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'