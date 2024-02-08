from experience.cat_part_interfaces import Sweep

class Rib(Sweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Sweep
                |                                 Rib
    """

    def __init__(self, com):
        super().__init__(com)
        self.rib = com

    def __repr__(self):
        return f'Rib(name="{self.name}")'