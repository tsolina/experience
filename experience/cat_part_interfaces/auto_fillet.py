from typing import Union, Optional, TYPE_CHECKING

from experience.inf_interfaces import Reference, References
from experience.cat_part_interfaces import DressUpShape

if TYPE_CHECKING:
    from experience.knowledge_interfaces import Length

class AutoFillet(DressUpShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             AutoFillet
    """

    def __init__(self, com):
        super().__init__(com)
        self.auto_fillet = com

    def curvature_radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.auto_fillet.CurvatureRadius)

    def faces_to_fillet(self) -> References:
        return References(self.auto_fillet.FacesToFillet)

    def faces_to_fillets(self, value: Reference) -> 'AutoFillet':
        self.auto_fillet.FacesToFillets = value._com
        return self

    def fillet_radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.auto_fillet.FilletRadius)

    def functional_face(self, reference: Reference) -> 'AutoFillet':
        self.auto_fillet.FunctionalFace = reference._com
        return self

    def functional_faces(self) -> References:
        return References(self.auto_fillet.FunctionalFaces)

    def parting_element(self, value: Reference = None) -> Union['AutoFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_fillet.PartingElement = value._com
            return self
        return Reference(self.auto_fillet.PartingElement)

    def round_radius(self) -> 'Length':
        from experience.knowledge_interfaces import Length
        return Length(self.auto_fillet.RoundRadius)

    def round_radius_activation(self, value: bool = None) -> Union['AutoFillet', bool]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_fillet.RoundRadiusActivation = value
            return self
        return self.auto_fillet.RoundRadiusActivation

    def slivers_and_crack(self, reference: Reference) -> 'AutoFillet':
        self.auto_fillet.SliversAndCrack = reference._com
        return self

    def slivers_and_cracks(self) -> References:
        return References(self.auto_fillet.SliversAndCracks)

    def support_surface(self, value: Reference = None) -> Union['AutoFillet', Reference]:
        """ set value if provided and return self, otherwise reads the value """
        if value is not None:
            self.auto_fillet.SupportSurface = value._com
            return self
        return Reference(self.auto_fillet.SupportSurface)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'