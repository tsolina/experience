from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeSpine(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSpine
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_spine = com

    def orientation(self, value: int = None) -> Union['HybridShapeSpine', int]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spine.Orientation = value
            return self
        return self.hybrid_shape_spine.Orientation

    def start_point(self, value: Reference = None) -> Union['HybridShapeSpine', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_spine.StartPoint = value._com
            return self
        return Reference(self.hybrid_shape_spine.StartPoint)

    def add_guide(self, i_guide: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.AddGuide(i_guide._com)
        return self

    def add_section(self, i_section: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.AddSection(i_section.com)
        return self
    
    def get_guide(self, i_idx: int) -> Reference:
        return self.hybrid_shape_spine.GetGuide(i_idx)

    def get_number_of_guides(self) -> int:
        return self.hybrid_shape_spine.GetNumberOfGuides()

    def get_number_of_sections(self) -> int:
        return self.hybrid_shape_spine.GetNumberOfSections()

    def get_section(self, i_idx: int) -> Reference:
        return self.hybrid_shape_spine.GetSection(i_idx)

    def modify_guide_curve(self, ip_ia_guide: Reference, ip_ia_new_guide: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.ModifyGuideCurve(ip_ia_guide._com, ip_ia_new_guide._com)
        return self

    def modify_section_curve(self, ip_ia_section: Reference, ip_ia_new_section: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.ModifySectionCurve(ip_ia_section._com, ip_ia_new_section._com)
        return self

    def remove_guide(self, i_guide: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.RemoveGuide(i_guide._com)
        return self

    def remove_section(self, i_section: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.RemoveSection(i_section._com)
        return self

    def set_start_point(self, i_point: Reference) -> 'HybridShapeSpine':
        self.hybrid_shape_spine.SetStartPoint(i_point._com)
        return self

    def __repr__(self):
        return f'HybridShapeSpine(name="{self.name}")'