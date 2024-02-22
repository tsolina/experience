from typing import Iterator, TYPE_CHECKING

from experience.system import AnyObject, Collection
from experience.knowledge_interfaces import Relation

if TYPE_CHECKING:
    from experience.types import cat_variant
    from experience.knowledge_interfaces import Check, DesignTable, Formula, Parameter, Law, Rule, SetOfEquation

class Relations(Collection):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Relations
    """

    def __init__(self, com):
        super().__init__(com, child=Relation)
        self.relations = com

    def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> 'Check':
        from experience.knowledge_interfaces import Check
        return Check(self.relations.CreateCheck(i_name, i_comment, i_check_body))
    
    def create_design_table_with_rep_ref(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_ref: AnyObject) -> 'DesignTable':
        from experience.knowledge_interfaces import DesignTable
        return DesignTable(self.relations.CreateDesignTableWithRepRef(i_name, i_comment, i_copy_mode, i_sheet_ref._com))

    def create_formula(self, i_name: str, i_comment: str, i_output_parameter: 'Parameter', i_formula_body: str) -> 'Formula':
        from experience.knowledge_interfaces import Formula
        return Formula(self.relations.CreateFormula(i_name, i_comment, i_output_parameter._com, i_formula_body))

    def create_horizontal_design_table_with_rep_ref(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_ref: AnyObject) -> 'DesignTable':
        from experience.knowledge_interfaces import DesignTable
        return DesignTable(self.relations.CreateHorizontalDesignTableWithRepRef(i_name, i_comment, i_copy_mode, i_sheet_ref._com))

    def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> 'Law':
        from experience.knowledge_interfaces import Law
        return Law(self.relations.CreateLaw(i_name, i_comment, i_law_body))

    def create_program(self, i_name: str, i_comment: str, i_program_body: str) -> 'Rule':
        from experience.knowledge_interfaces import Rule
        return Rule(self.relations.CreateProgram(i_name, i_comment, i_program_body))

    def create_rule_base(self, i_name: str) -> Relation:
        return Relation(self.relations.CreateRuleBase(i_name))

    def create_set_of_equations(self, i_name: str, i_comment: str, i_formula_body: str) -> 'SetOfEquation':
        from experience.knowledge_interfaces import SetOfEquation
        return SetOfEquation(self.relations.CreateSetOfEquations(i_name, i_comment, i_formula_body))

    def create_set_of_relations(self, i_parent: AnyObject) -> 'Relations':
        self.relations.CreateSetOfRelations(i_parent._com)
        return self

    def generate_xml_report_for_checks(self, i_name: str) -> 'Relations':
        self.relations.GenerateXMLReportForChecks(i_name)
        return self

    def item(self, i_index: 'cat_variant') -> Relation:
        return Relation(self.relations.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> None:
        return self.relations.Remove(i_index)

    def sub_list(self, i_feature: AnyObject, i_recursively: bool) -> 'Relations':
        return Relations(self.relations.SubList(i_feature._com, i_recursively))

    def __getitem__(self, n: int) -> Relation:
        if (n + 1) > self.count():
            raise StopIteration

        return Relation(self.relations.item(n + 1))

    def __iter__(self) -> Iterator[Relation]:
        for i in range(self.count()):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name()}")'