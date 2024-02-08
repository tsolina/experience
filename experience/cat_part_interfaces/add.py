from experience.cat_part_interfaces import BooleanShape

class Add(BooleanShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Add
    """

    def __init__(self, com):
        super().__init__(com)
        self.add = com

    def __repr__(self):
        return f'Add(name="{self.name}")'