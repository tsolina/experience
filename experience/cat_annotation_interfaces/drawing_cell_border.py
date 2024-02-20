from typing import Union

class DrawingCellBorder():
    def __init__(self, value: int = 0, i_row: int = 1, i_col: int = 1) -> None:
        self._row = i_row
        self._col = i_col
        self.reset()
        self._set_values(value)

    def _set_values(self, value: int):
        if value == 0:
            return
        
        bin_value = bin(value)[2:]
        num_zeros = max(0, 6 - len(bin_value))
        bin_value = '0' * num_zeros + bin_value

        self._slash = bin_value[0]
        self._backslash = bin_value[1]
        self._bottom = bin_value[2]
        self._right = bin_value[3]
        self._top = bin_value[4]
        self._left = bin_value[5]

    def value(self, i_value: int = None) -> Union['DrawingCellBorder', int]:
        if i_value is not None:
            self._set_values(i_value)
            return self
        
        rVal = "".join([self._slash, self._backslash, self._bottom, self._right, self._top, self._left])
        return int(rVal, 2)

    def set_value(self, i_left: bool, i_top: bool, i_right: bool, i_bottom: bool, i_backslash: bool, i_slash: bool) -> 'DrawingCellBorder':
        self._left = str(int(i_left))
        self._top = str(int(i_top))
        self._right = str(int(i_right))
        self._bottom = str(int(i_bottom))
        self._backslash = str(int(i_backslash))
        self._slash = str(int(i_slash))
        return self
    
    def reset(self) -> 'DrawingCellBorder':
        self._left = "0"
        self._top = "0"
        self._right = "0"
        self._bottom = "0"
        self._backslash = "0"
        self._slash = "0"
        return self
    
    def activate_all(self) -> 'DrawingCellBorder':
        self._left = "1"
        self._top = "1"
        self._right = "1"
        self._bottom = "1"
        self._backslash = "1"
        self._slash = "1"
        return self

    def get_edges(self) -> tuple:
        return ("left:" + self._left, "top: " + self._top, "right: " + self._right, "bottom: " + self._bottom, "backslash: " + self._backslash, "slash: " + self._slash) 

    def left(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._left = str(int(value))
            return self
        return bool(self._left)  
    
    def top(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._top = str(int(value))
            return self
        return bool(self._top)
    
    def right(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._right = str(int(value))
            return self
        return bool(self._right)

    def bottom(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._bottom = str(int(value))
            return self
        return bool(self._bottom)
    
    def backslash(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._backslash = str(int(value))
            return self
        return bool(self._backslash)
    
    def slash(self, value: bool = None) -> Union['DrawingCellBorder', bool]:
        if value is not None:
            self._slash = str(int(value))
            return self
        return bool(self._slash)
    
    def row(self, value: int = None) -> Union['DrawingCellBorder', int]:
        if value is not None:
            self._row = value
            return self
        return self._row
    
    def col(self, value: int = None) -> Union['DrawingCellBorder', int]:
        if value is not None:
            self._col = value
            return self
        return self._col

    def __repr__(self):
        return f'DrawingCellBorder({self.value()}: "{self.get_edges()}")'

if __name__ == "__main__":
    border = DrawingCellBorder(18, 1, 1)
    print(border.get_edges())
    print(border.top(), border.value())

    border2 = DrawingCellBorder(0).top(True).right(True).slash(True)
    print(border2.value())
    print(border2)

    border3 = DrawingCellBorder(21)
    print(border3)