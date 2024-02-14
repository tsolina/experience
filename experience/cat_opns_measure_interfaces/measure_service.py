from typing import Union, Optional, TYPE_CHECKING

from experience.system import AnyObject
from experience.inf_interfaces import Service

if TYPE_CHECKING:
    from experience.cat_opns_measure_interfaces import MeasureBetween, MeasureItem

class MeasureService(Service):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         MeasureService
    """

    def __init__(self, com):
        super().__init__(com)
        self.measure_service = com

    def get_measure_between(self, i_first_selection: tuple, i_second_selection: tuple) -> 'MeasureBetween':
        from experience.cat_opns_measure_interfaces import MeasureBetween
        return MeasureBetween(self.measure_service.GetMeasureBetween(i_first_selection, i_second_selection))
    
    def get_measure_item(self, i_selections: tuple) -> 'MeasureItem':
        from experience.cat_opns_measure_interfaces import MeasureItem
        return MeasureItem(self.measure_service.GetMeasureItem(i_selections))

    def __repr__(self):
        return f'MeasureService(name="{self.name()}")'