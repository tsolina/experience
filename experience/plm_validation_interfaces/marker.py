from typing import TYPE_CHECKING, Union
from experience.system import AnyObject
from experience.plm_validation_interfaces.plm_validation_types import *

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Angle
    from experience.plm_validation_interfaces import MarkerPointing

class Marker(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Marker
    """

    def __init__(self, com):
        super().__init__(com)
        self.marker = com

    def angle(self, value: 'Angle' = None) -> Union['Marker', 'Angle']:
        if value is not None:
            self.marker.Angle = value._com
            return self
        from experience.knowledge_interfaces import Angle
        return self.marker.Angle
    
    def document_ref(self, i_reference: str) -> 'Marker':
        self.marker.DocumentRef = i_reference
        return self
    
    def fill(self, value: bool = None) -> Union['Marker', bool]:
        if value is not None:
            self.marker.Fill = value
            return self
        return self.marker.Fill
    
    def frame(self, value: bool = None) -> Union['Marker', bool]:
        if value is not None:
            self.marker.Frame = value
            return self
        return self.marker.Frame
    
    def type(self) -> PLMMarkerType:
        return PLMMarkerType.item(self.marker.Type)

    def get_pointing(self) -> 'MarkerPointing':
        from experience.plm_validation_interfaces import MarkerPointing
        return MarkerPointing(self.marker.GetPointing())
    
    def get_positions(self) -> tuple:
        s_type = self.type()
        if s_type in {PLMMarkerType.Line2D, PLMMarkerType.Arrow2D, PLMMarkerType.Rectangle2D, PLMMarkerType.Circle2D}:
            return self._get_safe_array_multi(self.marker, "GetPositions", 3)
        elif s_type in {PLMMarkerType.Text3D, PLMMarkerType.Picture3D, PLMMarkerType.Hyperlink3D, PLMMarkerType.Audio3D}:
            return self._get_safe_array(self.marker, "GetPositions", 2)
        elif s_type in {PLMMarkerType.Text2D, PLMMarkerType.Picture2D, PLMMarkerType.Hyperlink2D, PLMMarkerType.Audio2D}:
            return self._get_safe_array(self.marker, "GetPositions", 1)
        else:
            return self._get_safe_array(self.marker, "GetPositions", 100)
        
    def is_pointing(self) -> bool:
        return self.marker.IsPointing()
    
    def set_positions(self, i_coordinates: tuple) -> 'Marker':
        self.marker.SetPositions(i_coordinates)
        return self
    
    def update(self) -> 'Marker':
        self.marker.Update()
        return self