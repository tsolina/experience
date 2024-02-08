from experience.cat_part_interfaces import Sweep

class Slot(Sweep):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Sweep
                |                                 Slot
    """

    def __init__(self, com):
        super().__init__(com)
        self.slot = com

    def __repr__(self):
        return f'Slot(name="{self.name}")'