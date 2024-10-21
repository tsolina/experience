from typing import Iterator, TYPE_CHECKING, Union

from .cat_sim_rep_types import *
from experience.system import AnyObject

class SimXRep(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimXRep
    """

    def __init__(self, com):
        super().__init__(com)
        self.sim_x_rep = com

    def file_name(self, value: str = None) -> Union["SimXRep", str]:
        if value is not None:
            self.sim_x_rep.FileName = value
            return self
        return self.sim_x_rep.FileName
    
    def nav_rep_name(self, value: str = None) -> Union["SimXRep", str]:
        if value is not None:
            self.sim_x_rep.NavRepName = value
            return self
        return self.sim_x_rep.NavRepName
    
    def add_relation(self, i_pointed_object: AnyObject, i_relation_type: SimXRepRelationType) -> 'SimXRep':
        self.sim_x_rep.AddRelation(i_pointed_object._com, int(i_relation_type))
        return self
    
    def export_file(self, i_folder_path: str) -> 'SimXRep':
        self.sim_x_rep.ExportFile(i_folder_path)
        return self
    
    def export_nav_rep(self, i_folder_path: str) -> 'SimXRep':
        self.sim_x_rep.ExportNavRep(i_folder_path)
        return self
    
    def generate_nav_rep(self, i_file_path: str, i_length_unit: str) -> 'SimXRep':
        self.sim_x_rep.GenerateNavRep(i_file_path, i_length_unit)
        return self
    
    def import_file(self, i_folder_path: str, i_keep_nav_rep: bool) -> 'SimXRep':
        self.sim_x_rep.ImportFile(i_folder_path, i_keep_nav_rep)
        return self
    
    def import_nav_rep(self, i_folder_path: str) -> 'SimXRep':
        self.sim_x_rep.ImportNavRep(i_folder_path)
        return self
    
    def remove_relation(self, i_relation_pointed_object: AnyObject) -> 'SimXRep':
        self.sim_x_rep.RemoveRelation(i_relation_pointed_object._com)
        return self
        
    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'