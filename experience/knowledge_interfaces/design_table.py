from typing import Union, TYPE_CHECKING
from experience.knowledge_interfaces import Relation
from experience.knowledge_interfaces.knowledge_types import *


if TYPE_CHECKING:
    from experience.system import AnyObject
    from experience.knowledge_interfaces import Parameter

class DesignTable(Relation):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                         KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 DesignTable
    """

    def __init__(self, com):
        super().__init__(com)
        self.design_table = com

    def columns_nb(self) -> int:
        return self.design_table.ColumnsNb
    
    def configuration(self, value: int = None) -> Union['DesignTable', int]:
        if value is not None:
            self.design_table.Configuration = value
            return self
        return self.design_table.Configuration
    
    def configuration_nb(self) -> int:
        return self.design_table.ConfigurationsNb
    
    def copy_mode(self, value: bool = None) -> Union['DesignTable', bool]:
        if value is not None:
            self.design_table.CopyMode = value
            return self
        return self.design_table.CopyMode
    
    def file_path(self) -> str:
        # deprecated
        return self.design_table.FilePath
    
    def sheet_rep_ref(self, value: 'AnyObject' = None) -> Union['DesignTable', 'AnyObject']:
        if value is not None:
            self.design_table.Configuration = value._com
            return self
        from experience.system import AnyObject
        return AnyObject(self.design_table.Configuration)
    
    def add_association(self, i_parameter: 'Parameter', i_sheet_column: str) -> 'DesignTable':
        self.design_table.AddAssociation(i_parameter._com, i_sheet_column)
        return self
    
    def add_new_row(self) -> 'DesignTable':
        self.design_table.AddNewRow()
        return self
    
    def cell_as_string(self, i_row: int, i_column: int) -> str:
        return self.design_table.CellAsString(i_row, i_column)
    
    def remove_association(self, i_sheet_column: str) -> 'DesignTable':
        self.design_table.RemoveAssociation(i_sheet_column)
        return self
    
    def synchronize(self) -> 'DesignTable':
        self.design_table.Synchronize()
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'