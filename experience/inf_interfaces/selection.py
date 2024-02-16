from typing import Iterator, TYPE_CHECKING
from experience.system import AnyObject
from experience.inf_interfaces import SelectedElement

if TYPE_CHECKING:
    from experience.inf_interfaces import VisPropertySet, Editor

class Selection(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Selection
    """

    def __init__(self, com, child=SelectedElement):
        super().__init__(com)
        self.selection = com
        self._child = child

    def count(self) -> int:
        return self.selection.Count

    #deprecated
    def count2(self) -> int:
        return self.selection.Count

    def vis_properties(self) -> 'VisPropertySet':
        from experience.inf_interfaces import VisPropertySet
        return VisPropertySet(self.selection.VisProperties).set_parent(self)

    def add(self, i_object: AnyObject) -> 'Selection':
        self.selection.Add(i_object._com)
        return self

    def clear(self) -> 'Selection':
        self.selection.Clear()
        return self

    def copy(self) -> 'Selection':
        self.selection.Copy()
        return self

    def cut(self) -> 'Selection':
        self.selection.Cut()
        return self

    def delete(self) -> 'Selection':
        if self.count() != 0:
            self.selection.Delete()
        return self

    def filter_correspondence(self, i_filter_type: tuple) -> bool:
        return self.selection.FilterCorrespondence(i_filter_type)

    def find_object(self, i_object_type: str) -> AnyObject:
        return AnyObject(self.selection.FindObject(i_object_type))

    def indicate_or_select_element_2d(self, i_message: str, i_filter_type: tuple, i_object_selection_before_command_use_possibility: bool, i_tooltip: bool, i_triggering_on_mouse_move: bool, o_object_selected: bool, o_document_window_location: tuple) -> str:
        return self.selection.IndicateOrSelectElement2D(i_message, i_filter_type, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move, o_object_selected, o_document_window_location)

    def indicate_or_select_element_3d(self, i_planar_geometric_object: AnyObject, i_message: str, i_filter_type: tuple, i_object_selection_before_command_use_possibility: bool, i_tooltip: bool, i_triggering_on_mouse_move: bool) -> tuple:
        vba_function_name = 'indicate_or_select_element_3d'
        vba_code = f'''
        Public Function {vba_function_name}(selection, i_planar_geometric_object, i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move)
        Dim o_object_selected
        Dim o_window_location_2d (1)
        Dim o_window_location_3d (2)
        Dim o_output_state (3)
        o_output_state (0) = selection.IndicateOrSelectElement3D(i_planar_geometric_object, i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move, o_object_selected, o_window_location_2d, o_window_location_3d)
        o_output_state (1) = o_object_selected
        o_output_state (2) = o_window_location_2d
        o_output_state (3) = o_window_location_3d
        {vba_function_name} = o_output_state
        End Function
        '''

        system_service = self.application.system_service
        result = system_service.evaluate(vba_code,
                                         0,
                                         vba_function_name,
                                         [
                                             self.selection,
                                             i_planar_geometric_object._com,
                                             i_message, i_filter_type,
                                             i_object_selection_before_command_use_possibility,
                                             i_tooltip,
                                             i_triggering_on_mouse_move

                                         ]
                                         )

        return result

    def item(self, i_index: int) -> SelectedElement:
        return SelectedElement(self.selection.Item(i_index))

    #deprecated
    def item2(self, i_index: int) -> SelectedElement:
        return SelectedElement(self.selection.Item(i_index))

    def items(self) -> tuple:
        items_list = []
        for i in range(self._com.Count):
            item = self._child(self._com.Item(i + 1))
            items_list.append(item)

        return items_list

    def paste(self) -> 'Selection':
        self.selection.Paste()
        return self

    def paste_special(self, i_format: str) -> 'Selection':
        self.selection.PasteSpecial(i_format)
        return self

    def remove(self, i_index: int) -> 'Selection':
        self.selection.Remove(i_index)
        return self

    #deprecated
    def remove2(self, i_index: int) -> 'Selection':
        self.selection.Remove(i_index)
        return self

    def search(self, i_string_bstr: str) -> 'Selection':
        self.selection.Search(i_string_bstr)
        return self

    def select_element(self, i_filter_type: tuple, i_message: str, i_may_skip_interactive_selection: bool) -> str:
        # check_type(i_filter_type, tuple)
        return self.selection.SelectElement(i_filter_type, i_message, i_may_skip_interactive_selection)

    #deprecated
    def select_element2(self, i_filter_type: tuple, i_message: str, i_object_selection_before_command_use_possibility: bool) -> str:
        # check_type(i_filter_type, tuple)
        return self.selection.SelectElement2(i_filter_type, i_message, i_object_selection_before_command_use_possibility)

    #deprecated
    def select_element3(self, i_filter_type: tuple, i_message: str, i_object_selection_before_command_use_possibility: bool, i_multi_selection_mode: int, i_tooltip: bool) -> str:
        # check_type(i_filter_type, tuple)
        return self.selection.SelectElement3(i_filter_type, i_message, i_object_selection_before_command_use_possibility, i_multi_selection_mode, i_tooltip)

    def select_element_other_editor(self, i_filter_type: tuple, i_active_editor_message: str, i_non_active_editor_message: str, i_tooltip: bool, oEditor: 'Editor') -> str:
        return self.selection.SelectElementOtherEditor(i_filter_type, i_active_editor_message, i_non_active_editor_message, i_tooltip, oEditor._com)

    def __len__(self):
        return self.count

    def __getitem__(self, n: int) -> SelectedElement:
        if (n + 1) > self.count:
            raise StopIteration

        return SelectedElement(self.selection.item(n + 1))

    def __iter__(self) -> Iterator[SelectedElement]:
        for i in range(self.count):
            yield self._child(self._com.item(i + 1))

    def __repr__(self):
        return f'Selection(name="{self.name()}")'
