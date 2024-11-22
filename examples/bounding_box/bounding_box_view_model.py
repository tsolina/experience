import tkinter as tk
from examples.bounding_box.bounding_box_model import BoundingBoxModel

class BoundingBoxViewModel:
    def __init__(self, model: 'BoundingBoxModel'):
        self._model = model
        self.set_defaults()

    def set_defaults(self):
        self.cb_all_var = tk.IntVar(value=0)
        self.cb_x_var = tk.IntVar()
        self.cb_y_var = tk.IntVar()
        self.cb_z_var = tk.IntVar()

        self.nx_var = tk.StringVar()
        self.ny_var = tk.StringVar()
        self.nz_var = tk.StringVar()
        self.px_var = tk.StringVar()
        self.py_var = tk.StringVar()
        self.pz_var = tk.StringVar()

        self.nx_var.trace_add("write", self.on_nx_value_changed)
        self.px_var.trace_add("write", self.on_px_value_changed)
        self.ny_var.trace_add("write", self.on_ny_value_changed)
        self.py_var.trace_add("write", self.on_py_value_changed)
        self.nz_var.trace_add("write", self.on_nz_value_changed)
        self.pz_var.trace_add("write", self.on_pz_value_changed)

        self.is_updating = False
        self.shape_name_var = tk.StringVar()
        self.axis_name_var = tk.StringVar()

    def on_nx_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.nx_var.get()) if self.nx_var.get() != "" else 0.0
        self._model.set_nx_value(val)
        if self.cb_x_var.get() == 1:
            self.is_updating = True
            self.px_var.set(val)
            self.is_updating = False

    def on_px_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.px_var.get()) if self.px_var.get() != "" else 0.0
        self._model.set_px_value(val)
        if self.cb_x_var.get() == 1:
            self.is_updating = True
            self.nx_var.set(val)
            self.is_updating = False

    def on_ny_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.ny_var.get()) if self.ny_var.get() != "" else 0.0
        self._model.set_ny_value(val)
        if self.cb_y_var.get() == 1:
            self.is_updating = True
            self.py_var.set(val)
            self.is_updating = False

    def on_py_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.py_var.get()) if self.py_var.get() != "" else 0.0
        self._model.set_py_value(val)
        if self.cb_y_var.get() == 1:
            self.is_updating = True
            self.ny_var.set(val)
            self.is_updating = False

    def on_nz_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.nz_var.get()) if self.nz_var.get() != "" else 0.0
        self._model.set_nz_value(val)
        if self.cb_z_var.get() == 1:
            self.is_updating = True
            self.pz_var.set(val)
            self.is_updating = False

    def on_pz_value_changed(self, *args):
        if self.is_updating:
            return
        
        val = float(self.pz_var.get()) if self.pz_var.get() != "" else 0.0
        self._model.set_pz_value(val)
        if self.cb_z_var.get() == 1:
            self.is_updating = True
            self.nz_var.set(val)
            self.is_updating = False

    def get_entry_state_option_nx(self):
        return tk.DISABLED if self.cb_all_var.get() == 1 else tk.NORMAL
    
    def set_select_all_state(self):
        self._model.cb_same = self.cb_all_var.get()
        if self.cb_all_var.get() == False:
            self._model.nx_value = float(self.nx_var.get()) if self.nx_var.get() != "" else 0.0
            self._model.px_value = float(self.px_var.get()) if self.px_var.get() != "" else 0.0
            self._model.ny_value = float(self.ny_var.get()) if self.ny_var.get() != "" else 0.0
            self._model.py_value = float(self.py_var.get()) if self.py_var.get() != "" else 0.0
            self._model.pz_value = float(self.pz_var.get()) if self.pz_var.get() != "" else 0.0
            self._model.nz_value = float(self.nz_var.get()) if self.nz_var.get() != "" else 0.0
    
    def validate_input(self, new_value):
        if new_value == "" or new_value.isdigit() or new_value == "." or (new_value.replace('.', '', 1).isdigit() and new_value.count('.') <= 1):
            return True
        else:
            return False

    def same_value(self, cb_var: tk.IntVar, in_entry: tk.Entry, out_entry: tk.Entry):
        if cb_var.get() == 1:
            val = in_entry.get()
            val = float(val) if val != "" else 0.0
            out_entry.delete(0, tk.END)
            out_entry.insert(0, val)

            if cb_var == self.cb_x_var:
                self._model.set_cb_x_value = val
            elif cb_var == self.cb_y_var:
                self._model.set_cb_y_value = val
            elif cb_var == self.cb_z_var:
                self._model.set_cb_z_value = val

    def select_shape(self):
        shape_name = self._model.select_shape()
        self.shape_name_var.set(shape_name)

    def select_axis(self):
        axis_name = self._model.select_axis()
        self.axis_name_var.set(axis_name)

    def execute(self):
        self._model.execute()