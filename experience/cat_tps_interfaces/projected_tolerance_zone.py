from experience.system import AnyObject


class ProjectedToleranceZone(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProjectedToleranceZone
    """

    def __init__(self, com):
        super().__init__(com)
        self.projected_tolerance_zone = com

    def length(self) -> float:
        return self.projected_tolerance_zone.Length

    def position(self) -> float:
        return self.projected_tolerance_zone.Position

    def get_projected_tol_zone_reference(self) -> tuple: #, op_reference: tuple
        return self.projected_tolerance_zone.GetProjectedTolZoneReference()