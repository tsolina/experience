from experience.cat_part_interfaces import BooleanShape

class Intersect(BooleanShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Intersect
    """

    def __init__(self, com):
        super().__init__(com)
        self.intersect = com

    def __repr__(self):
        return f'Intersect(name="{self.name}")'