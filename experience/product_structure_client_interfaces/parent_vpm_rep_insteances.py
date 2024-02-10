from experience.plm_modeler_base_interfaces import PLMEntities

class ParentVPMRepInstances(PLMEntities):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMEntities
                |                       ParentVPMRepInstances 
    """

    def __init__(self, com):
        super().__init__(com)
        self.parent_vpm_rep_instances = com

    def __repr__(self):
        return f'ParentVPMRepInstances(name="{self.name}")'