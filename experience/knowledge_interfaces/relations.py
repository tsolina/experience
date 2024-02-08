from typing import Iterator, TYPE_CHECKING
from pathlib import Path

from experience.exceptions import CATIAApplicationException
# from pycatia.knowledge_interfaces.check import Check
# from pycatia.knowledge_interfaces.design_table import DesignTable
# from pycatia.knowledge_interfaces.formula import Formula
# from pycatia.knowledge_interfaces.law import Law
# from pycatia.knowledge_interfaces.optimizations import Optimizations
# from pycatia.knowledge_interfaces.relation import Relation
# from pycatia.knowledge_interfaces.rule import Rule
# from pycatia.knowledge_interfaces.set_of_equation import SetOfEquation
from experience.system import AnyObject, Collection
from experience.knowledge_interfaces import Relation

if TYPE_CHECKING:
    from experience.types import cat_variant

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
        super().__init__(com, _child=Relation)
        self.relations = com

    # def optimizations(self) -> Optimizations:
    #     return Optimizations(self.relations.Optimizations)

    # def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> Check:
    #     return Check(self.relations.CreateCheck(i_name, i_comment, i_check_body))

    # def create_design_table(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_path: Path) -> DesignTable:
    #     if not i_sheet_path.exists():
    #         raise CATIAApplicationException(f'Could not find design table "{i_sheet_path}".')

    #     return DesignTable(self.relations.CreateDesignTable(i_name, i_comment, i_copy_mode, i_sheet_path))

    # def create_formula(self, i_name, i_comment, i_output_parameter, i_formula_body):
    #     return Formula(self.relations.CreateFormula(i_name, i_comment, i_output_parameter.com_object, i_formula_body))

    # def create_horizontal_design_table(self,
    #                                    i_name: str,
    #                                    i_comment: str,
    #                                    i_copy_mode: bool,
    #                                    i_sheet_path: str) -> DesignTable:
    #     return DesignTable(self.relations.CreateHorizontalDesignTable(i_name, i_comment, i_copy_mode, i_sheet_path))

    # def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> Law:
    #     return Law(self.relations.CreateLaw(i_name, i_comment, i_law_body))

    # def create_program(self, i_name: str, i_comment: str, i_program_body: str) -> Rule:
    #     return Rule(self.relations.CreateProgram(i_name, i_comment, i_program_body))

    def create_rule_base(self, i_name: str) -> Relation:
        return Relation(self.relations.CreateRuleBase(i_name))

    # def create_set_of_equations(self, i_name: str, i_comment: str, i_formula_body: str) -> SetOfEquation:
    #     return SetOfEquation(self.relations.CreateSetOfEquations(i_name, i_comment, i_formula_body))

    def create_set_of_relations(self, i_parent: AnyObject) -> None:
        return self.relations.CreateSetOfRelations(i_parent._com)

    def generate_xml_report_for_checks(self, i_name: str) -> None:
        return self.relations.GenerateXMLReportForChecks(i_name)

    def item(self, i_index: 'cat_variant') -> Relation:
        return Relation(self.relations.Item(i_index))

    def remove(self, i_index: 'cat_variant') -> None:
        return self.relations.Remove(i_index)

    def sub_list(self, i_feature: AnyObject, i_recursively: bool) -> 'Relations':
        return Relations(self.relations.SubList(i_feature._com, i_recursively))

    def __getitem__(self, n: int) -> Relation:
        if (n + 1) > self.count:
            raise StopIteration

        return Relation(self.relations.item(n + 1))

    def __iter__(self) -> Iterator[Relation]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Relations(name="{self.name}")'