from experience.cat_part_interfaces import Prism

class Pad(Prism):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Prism
                |                                 Pad
    """

    def __init__(self, com):
        super().__init__(com)
        self.pad = com

    def __repr__(self):
        return f'Pad(name="{self.name}")'