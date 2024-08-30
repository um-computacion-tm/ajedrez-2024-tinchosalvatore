from main.exceptions import *

class ReglasDeMovimientos:

    def __init__(self):
        pass 

    def vertical_move(self, from_row, from_col, to_row, to_col):
        if from_col != to_col:
            1 if to_row > from_row else -1
    
    def horizontal_move(self, from_row, from_col, to_row, to_col):
        if from_row != to_row:
            1 if to_col > from_col else -1

    def vertical_horizontal_move(self, from_row, from_col, to_row, to_col):
        if from_row != to_row and from_col != to_col:
            raise InvalidMoveVerticalHorizontal("Esta pieza solo puede moverse en vertical o horizontal")
        if from_row != to_row:
            return self.vertical_move(from_row, from_col, to_row, to_col)
        else:
            return self.horizontal_move(from_row, from_col, to_row, to_col)
    
    def diagonal_move(self, from_row, from_col, to_row, to_col):
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if row_diff != col_diff:
            raise InvalidMoveDiagonal("Esta pieza solo puede moverse en diagonal")
        else:
            1 if to_row > from_row else -1
            1 if to_col > from_col else -1