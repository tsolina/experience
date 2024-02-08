from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference
from experience.mecmod_interfaces import HybridShape

class HybridShapeSection(HybridShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSection
    """

    def __init__(self, com):
        super().__init__(com)
        self.hybrid_shape_section = com

    def section_plane(self, value: Reference = None) -> Union['HybridShapeSection', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.hybrid_shape_section.SectionPlane = value._com
            return self
        return Reference(self.hybrid_shape_section.SectionPlane)

    def __repr__(self):
        return f'HybridShapeSection(name="{self.name}")'