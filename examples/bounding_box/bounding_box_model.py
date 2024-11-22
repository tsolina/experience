from typing import Union
from experience import *
from examples.bounding_box.bounding_box import BoundingBox

class BoundingBoxModel:
    def __init__(self, catia_com: Application = None, name=""):
        self._name = name
        self._px_value = 0
        self._py_value = 0
        self._pz_value = 0
        self._nx_value = 0
        self._ny_value = 0
        self._nz_value = 0
        self._cb_same = False
        self._cb_x = False
        self._cb_y = False
        self._cb_z = False
        self._shape_name = ""
        self._axis_name = ""
        self.bbox = BoundingBox(catia_com)

    @property
    def shape_name(self) -> str:
        return self._shape_name
    @shape_name.setter
    def shape_name(self, value: str) -> 'BoundingBoxModel':
        self.shape_name = value
        return self
    
    @property
    def axis_name(self) -> str:
        return self._axis_name
    @axis_name.setter
    def axis_name(self, value: str) -> 'BoundingBoxModel':
        self.axis_name = value
        return self

    def select_shape(self):
        print("shape selection")
        self._shape_name = self.bbox.select_shape()
        return self.shape_name

    def select_axis(self):
        print("axis selection")
        self._axis_name = self.bbox.select_axis()
        return self.axis_name

    @property
    def px_value(self) -> float:
        return self._px_value
    @px_value.setter
    def px_value(self, value: float):
        self._px_value = float(value)

    @property
    def py_value(self) -> float:
        return self._py_value
    @py_value.setter
    def py_value(self, value: float):
        self._py_value = float(value)
    
    @property
    def pz_value(self) -> float:
        return self._pz_value
    @pz_value.setter
    def pz_value(self, value: float):
        self._pz_value = float(value)
    
    @property
    def nx_value(self) -> float:
        return self._nx_value
    @nx_value.setter
    def nx_value(self, value: float):
        self._nx_value = float(value)
    
    @property
    def ny_value(self) -> float:
        return self._ny_value
    @ny_value.setter
    def ny_value(self, value: float):
        self._ny_value = float(value)
    
    @property
    def nz_value(self) -> float:
        return self._nz_value
    @nz_value.setter
    def nz_value(self, value: float):
        self._nz_value = float(value)
    
    @property
    def cb_same(self) -> bool:
        return self._cb_same
    @cb_same.setter
    def cb_same(self, value: bool):
        self._cb_same = value
    
    def get_px_value(self) -> float:
        return self._px_value
    def set_px_value(self, value: float) -> 'BoundingBoxModel':
        self._px_value = value
        return self

    def get_py_value(self) -> float:
        return self._py_value
    def set_py_value(self, value: float) -> 'BoundingBoxModel':
        self._py_value = value
        return self
    
    def get_pz_value(self) -> float:
        return self._pz_value
    def set_pz_value(self, value: float) -> 'BoundingBoxModel':
        self._pz_value = value
        return self
    
    def get_nx_value(self) -> float:
        return self._nx_value
    def set_nx_value(self, value: float) -> 'BoundingBoxModel':
        # prfloat("nx:" + value)
        self._nx_value = value
        return self
    
    def get_ny_value(self) -> float:
        return self._ny_value
    def set_ny_value(self, value: float) -> 'BoundingBoxModel':
        self._ny_value = value
        return self
    
    def get_nz_value(self) -> float:
        return self._nz_value
    def set_nz_value(self, value: float) -> 'BoundingBoxModel':
        self._nz_value = value
        return self
    
    def set_cb_x_value(self, value: bool) -> 'BoundingBoxModel':
        self._cb_x = value
        return self

    def set_cb_y_value(self, value: bool) -> 'BoundingBoxModel':
        self._cb_y = value
        return self
    
    def set_cb_z_value(self, value: bool) -> 'BoundingBoxModel':
        self._cb_z = value
        return self
    
    def adjust_input_values(self):
        if self._cb_same == True:
            print(self.nx_value)
            self.nx_value = self.px_value
            print(self.nx_value)
            self.ny_value = self.px_value
            self.py_value = self.px_value
            self.nz_value = self.px_value
            self.pz_value = self.px_value
        else:
            print("input false")
            print(self.nx_value)
    
    def execute(self):
        self.adjust_input_values()
        self.bbox.execute(self)
    



    def name(self, value: str = None) -> Union['BoundingBoxModel', str]:
        if value is not None:
            self._name = value
            return self
        return self._name