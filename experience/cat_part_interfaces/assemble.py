from experience.cat_part_interfaces import BooleanShape

class Assemble(BooleanShape):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Assemble
    """

    def __init__(self, com):
        super().__init__(com)
        self.assemble = com

    def __repr__(self):
        return f'Assemble(name="{self.name}")'