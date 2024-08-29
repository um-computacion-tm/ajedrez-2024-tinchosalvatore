from main.exceptions import *

# class ReglasDeMovimientos:

    #def __init__(self) -> None:
    #    ...
#
    #def vertical_move(self, to_row, to_col, board):
    #        from_row, from_col = self.get_position()
    #        if from_col != to_col:
    #            return False
#
    #        step = 1 if to_row > from_row else -1
    #        for row in range(from_row + step, to_row, step):
    #            if board.get_piece(row, from_col) is not None:
    #                return False
    #        return True
#
    #def horizontal_move(self, to_row, to_col, board):
    #    from_row, from_col = self.get_position()
    #    if from_row != to_row:
    #        return False
#
    #    step = 1 if to_col > from_col else -1
    #    for col in range(from_col + step, to_col, step):
    #        if board.get_piece(from_row, col) is not None:
    #            return False
    #    return True
#
    #def diagonal_move(self, to_row, to_col, board):
    #    from_row, from_col = self.get_position()
    #    row_diff = abs(to_row - from_row)
    #    col_diff = abs(to_col - from_col)
    #    if row_diff != col_diff:
    #        return False
#
    #    row_step = 1 if to_row > from_row else -1
    #    col_step = 1 if to_col > from_col else -1
    #    for step in range(1, row_diff):
    #        if board.get_piece(from_row + step * row_step, from_col + step * col_step) is not None:
    #            return False
    #    return True
    
