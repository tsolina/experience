from typing import Iterator, TYPE_CHECKING, Union

from experience.system import AnyObject

if TYPE_CHECKING:
    from experience.cat_sim_rep_interfaces.sim_parameter_set import SimParameterSet

class SimImportExportArgs(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimImportExportArgs
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_import_export_args = com
        
    def parameters(self) -> 'SimParameterSet':
        from experience.cat_sim_rep_interfaces.sim_parameter_set import SimParameterSet
        return SimParameterSet(self.sim_import_export_args.Parameters)
    
    def set_path(self, i_path: str) -> 'SimImportExportArgs':
        self.sim_import_export_args.SetPath(i_path)
        return self
    
    def set_units(self, i_magnitudes: list, i_units: list) -> 'SimImportExportArgs':
        self.sim_import_export_args.SetUnits(i_magnitudes, i_units)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'