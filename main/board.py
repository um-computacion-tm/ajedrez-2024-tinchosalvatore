from main.rook import Rook
from main.knight import Knight
from main.bishop import Bishop
from main.queen import Queen
from main.king import King
from main.pawn import Pawn

class Board:

    #Board class is responsible for the board representation, and some small extra methods used later on

    def __init__(self):        
        self.__positions__ = self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
            
        self.initialize_board()
            
    def initialize_board(self):
        #Inicial position for evert black piece
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")

        #Inicial position for evert white piece
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][3] = Queen("WHITE")
        self.__positions__[7][4] = King("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        for i in range(8):
            self.__positions__[6][i] = Pawn("WHITE")
        
    
    #Setter for the pieces
    def set_piece(self, piece, row, col):
        self.__positions__[row][col] = piece
    
    #Getter for the pieces
    def get_piece(self, row, col):
        return self.__positions__[row][col]

    #Color getter for the pieces
    def get_color(self, row, col):
        piece =  self.get_piece(row, col)
        if piece is None:
            return None
        return piece.get_color()

    #Pawn getter to know if the piece is a pawn, used later on chess.py
    def get_pawn(self, row, col):
        piece =  self.get_piece(row, col)
        if piece is None:
            return None
        if isinstance(piece, Pawn):
            return piece
        return None

    #This method removes a piece from the indicated position
    def remove_piece(self, row, col):
        self.__positions__[row][col] = None
    
    def occupied_path_vertical_horizontal(self, from_row, from_col, to_row, to_col):
        #This method checks if the path is occupied for the movement that is going to be made
        #This method and the one below are used to check if the movement is valid, on chess.py        
        if from_row == to_row:#For horizontal movement
            start_col, end_col = sorted([from_col, to_col])
            for col in range(start_col + 1, end_col):
                if self.get_piece(from_row, col):
                    return True
        elif from_col == to_col:  #For vertical movement
            start_row, end_row = sorted([from_row, to_row])
            for row in range(start_row + 1, end_row):
                if self.get_piece(row, from_col):
                    return True
        return False
    
    def occupied_path_diagonal(self, from_row, from_col, to_row, to_col):
        #As it was said before, this method checks if the path is occupied for the movement that is going to be made
        #It used on chess.py
        if abs(from_row - to_row) == abs(from_col - to_col):  #Diagonal movement
            row_step = 1 if to_row > from_row else -1
            col_step = 1 if to_col > from_col else -1
            row, col = from_row + row_step, from_col + col_step
            while row != to_row and col != to_col:
                if self.get_piece(row, col):
                    return True
        return False


    #This method shows the board, its used to print it later on, and add numbers so the user can see the positions easily
    def show_board(self):
        #Shows the numbers of the columns in the upper part and in the lower part
        columns_numbers = "  " + " ".join([str(i) for i in range(8)])

        #Shows the rows of the board with the numbers to the left and to the right
        rows = "\n".join([f"{i} {' '.join([str(piece) if piece else '.' for piece in row])} {i}" for i, row in enumerate(self.__positions__)])

        #Combines all parts in the board representation
        board_representation = f"{columns_numbers}\n{rows}\n{columns_numbers}\n"

        return board_representation