from experience.system import AnyObject
from experience.inf_interfaces import References

class PartServices(AnyObject):
    #Set partServices1 = myPart.GetItem("CATPartServices")
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OriginElements
    """

    def __init__(self, com):
        super().__init__(com)
        self.part_services = com

    def get_near_sub_elements(self, i_object: AnyObject, i_sub_element_dimension: int, i_near_object: AnyObject) -> References:
        return References(self.part_services.GetNearSubElements(i_object._com, i_sub_element_dimension, i_near_object._com))
    
    def get_sub_elements(self, i_object: AnyObject, i_sub_element_dimension: int, i_duplicates: bool) -> References:
        return References(self.part_services.GetSubElements(i_object._com, i_sub_element_dimension, i_duplicates))
    
    def __repr__(self):
        return f'PartServices(name="{self.name()}")'