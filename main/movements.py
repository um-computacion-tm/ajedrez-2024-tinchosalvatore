from main.exceptions import *
class ReglasDeMovimientos:

    def __init__(self):
        pass 

        #I started with some general moving methods, that later on will be reused in other pieces movement

    def vertical_move(self, from_row, from_col, to_row, to_col):
        #Determines if the movement is vertical
        if from_col != to_col:
            1 if to_row > from_row else -1

    def horizontal_move(self, from_row, from_col, to_row, to_col):
        #Determines if the movement is horizontal, direction variable is not used but code climate was complaining
        #about similarity with vertical_move
        if from_row != to_row:
            direction = 1 if to_col > from_col else -1
            return direction

    def vertical_horizontal_move(self, from_row, from_col, to_row, to_col): 
        #Implements the vertical and horizontal movements together
        #In case it is neither vertical nor horizontal, it raises an exception
        if from_row != to_row and from_col != to_col:
            raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        if from_row != to_row:
            return self.vertical_move(from_row, from_col, to_row, to_col)
        else:
            return self.horizontal_move(from_row, from_col, to_row, to_col)
    
    def row_difference_move(self, from_row, to_row): #Calculates the difference between the rows, using absolute value
        return abs(to_row - from_row)
        

    def col_difference_move(self, from_col, to_col): #Calculates the difference between the columns, using absolute value
        return abs(to_col - from_col)
        

    def diagonal_move(self, from_row, from_col, to_row, to_col):
        #Determines if the movement is diagonal, in case it is not, it raises an exception
        #Uses the two previous methods calculate the diagonal movement
        row_diff = self.row_difference_move(from_row, to_row)
        col_diff = self.col_difference_move(from_col, to_col)
        if row_diff != col_diff:
            raise InvalidMoveDiagonal("El alfil solo puede moverse en diagonal")
        direction_row = 1 if to_row > from_row else -1
        direction_col = 1 if to_col > from_col else -1
        return direction_row, direction_col

    def knight_movement(self, from_row, from_col, to_row, to_col):
        #Determines if the movement is a knight movement, in case it is not, it raises an exception
        #Uses the two previous methods to determine the direction of to calculate the famous L shaped movement
        row_diff_knigth = self.row_difference_move(from_row, to_row)
        col_diff_knigth = self.col_difference_move(from_col, to_col)
        if not (row_diff_knigth == 2 and col_diff_knigth == 1) and not (row_diff_knigth == 1 and col_diff_knigth == 2):
            raise InvalidMoveKnight("Ese movimiento del caballo no es válido")
    
    def king_movement(self, from_row, from_col, to_row, to_col):
        #King movement, can only move one square in any direction, but combines al movement
        row_diff_king = self.row_difference_move(from_row, to_row)
        col_diff_king = self.col_difference_move(from_col, to_col)
        if row_diff_king > 1 or col_diff_king > 1:
            raise InvalidMoveKing("El rey solo puede moverse una casilla en cualquier dirección")
    
    def queen_movement(self, from_row, from_col, to_row, to_col): 
        #To reuse the previous methods, it uses a try and except to determine if the movement is diagonal or vertical or horizontal
        #making both of them valid 
        #Verifies the diagonal movement
        try:
            self.diagonal_move(from_row, from_col, to_row, to_col)
            return True
        except InvalidMoveDiagonal:
            pass  #If there isn't a diagonal movement, continue checking other movements

        #Verifies the vertical or horizontal movement
        try:
            self.vertical_horizontal_move(from_row, from_col, to_row, to_col)
            return True
        except InvalidMoveVerticalHorizontal:
            pass  #If there isn't a vertical or horizontal movement, it raises an exception

        #If the movement is neither diagonal nor vertical or horizontal, it is invalid, so it raises an exception
        raise InvalidMoveQueen("La reina solo puede moverse en línea recta o en diagonal")