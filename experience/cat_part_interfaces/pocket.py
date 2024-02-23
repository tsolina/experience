from experience.cat_part_interfaces import Prism

class Pocket(Prism):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Prism
                |                                 Pocket
    """

    def __init__(self, com):
        super().__init__(com)
        self.pocket = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'