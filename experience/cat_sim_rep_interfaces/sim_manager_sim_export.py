from typing import TYPE_CHECKING
from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_import_export_args import SimImportExportArgs

class SimManagerSIMExport(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimManagerSIMExport
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_manager_sim_export = com

    def args(self) -> 'SimImportExportArgs':
        from experience.cat_sim_rep_interfaces.sim_import_export_args import SimImportExportArgs
        return SimImportExportArgs(self.sim_manager_sim_export.Args)
    
    def export(self, i_exporter_id: str) -> 'SimManagerSIMExport':
        return self.sim_manager_sim_export.Export(i_exporter_id)
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'