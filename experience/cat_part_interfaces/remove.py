from experience.cat_part_interfaces import BooleanShape

class Remove(BooleanShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Remove
    """

    def __init__(self, com):
        super().__init__(com)
        self.remove = com

    def __repr__(self):
        return f'Remove(name="{self.name}")'