from experience.cat_part_interfaces import Revolution

class Groove(Revolution):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             PartInterfaces.Revolution
                |                                 Groove
    """

    def __init__(self, com):
        super().__init__(com)
        self.groove = com

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'