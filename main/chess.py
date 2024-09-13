from main.board import Board
from main.exceptions import *
from main.pawn import Pawn
from main.king import King

class Chess:

    #Chess class is very important for this program because here everything requested from the cli is done
    #Moves are validated here, and the board is updated
    #It also brings the way to end the game on cli

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True
        self.__pawn__ = Pawn


    def get_board(self): #This board getter is for helping tests to access the board
        return self.__board__


    def turn(self): #This method returns the current turn
        return self.__turn__

    def piece(self, from_row, from_col): #This method returns the piece in the position that is indicated
        piece = self.__board__.get_piece(from_row, from_col)
        return piece
    
    def target_piece(self, to_row, to_col): #This method returns the piece in the position that a piece is moving to
        return self.__board__.get_piece(to_row, to_col)

    #This method captures the piece in the indicated position
    #It uses remove_piece and set_piece methods from board.py to remove the captured piece and set the new piece in its position
    def capture_piece(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)
        if piece is None: #If piece is None, there is no capture done
            return None  

        if self.ocuppied_path(from_row, from_col, to_row, to_col): #Verifies if the path is occupied BEFORE validating the capture
            return 

        target_piece = self.target_piece(to_row, to_col)
        if target_piece and target_piece.get_color() != piece.get_color():
        #If checks if the captured piece is a from the other team, then removes it

            self.__board__.remove_piece(to_row, to_col) #Removes the captured piece
            self.__board__.set_piece(None, from_row, from_col) 
            self.__board__.set_piece(piece, to_row, to_col) #Sets the new piece
            return True
        return False
    
    # Special method for pawn capture
    def pawn_capture(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)
        if isinstance(piece, Pawn): #detects if the piece is a pawn
            there_is_a_piece = self.target_piece(to_row, to_col)
            if there_is_a_piece is not None and there_is_a_piece.get_color() != piece.get_color():
                #If there is a piece in the target position and it is not the same color as the pawn, it is a capture
                #So diagonal movement is validated in this case
                if piece.diagonal_pawn_movement(from_row, from_col, to_row, to_col):
                    self.__board__.remove_piece(to_row, to_col)
                    self.__board__.set_piece(None, from_row, from_col)
                    self.__board__.set_piece(piece, to_row, to_col)
                    return True
        return False

    def ocuppied_path(self, from_row, from_col, to_row, to_col):
        #This method calls occupied methods from board.py for the movement that is going to be made
        return self.__board__.occupied_path_vertical_horizontal(from_row, from_col, to_row, to_col) or \
            self.__board__.occupied_path_diagonal(from_row, from_col, to_row, to_col)
    
    def pieces_movements(self, from_row, from_col, to_row, to_col):
        #This method is used to validate the movement of the pieces
        #It was created so that the pawn could capture in diagonal but not in vertical
        #It also checks if the movement is valid for every piece
        piece = self.piece(from_row, from_col)
        target_piece = self.target_piece(to_row, to_col)
        if isinstance(piece, Pawn):
            if self.pawn_capture(from_row, from_col, to_row, to_col):
                self.change_turn()
                return True 
        
            elif not piece.valid_moves_pawn(from_row, from_col, to_row, to_col): #If pawn movement is not valid it raises an exception
                raise InvalidMoveNotAllowed("No es un movimiento válido para el peón")
            elif target_piece is not None: #If pawn vertical move has a piece on its destination it is not valid
                raise InvalidMoveNotAllowed("No es un movimiento válido para el peón")
        
        else:
                if not piece.valid_moves(from_row, from_col, to_row, to_col): #Checks valid moves for every piece
                    raise InvalidMoveNotAllowed("No es un movimiento válido para esa pieza")


    #This method is very important, because it calls all the methods that you have seen before and use them to move the pieces
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)

        if self.__board__.get_piece(from_row, from_col) is None: #Exceptions in case User tries to move an empty position
            raise InvalidMoveNoPiece("No hay pieza en esa posicion")
        
        if self.__turn__ != self.__board__.get_color(from_row, from_col): #Exceptions in case User tries to move a piece from other color
            raise InvalidMovePieceFromOtherColor("La pieza es del enemigo")

        if self.__turn__ == self.__board__.get_color(to_row, to_col): #Exceptions in case User tries to move a piece to a position with a same color piece
            raise InvalidMoveSameColor("La posicion tiene una pieza del mismo color")

        if self.king_dead(to_row, to_col): #Checks if the king is dead, if it is, it ends the game
                return
        
        if self.pieces_movements(from_row, from_col, to_row, to_col): #Calls pieces_movements method
            return
        
        if self.ocuppied_path(from_row, from_col, to_row, to_col): #Makes sure the path is not occupied
            raise InvalidMovePathOcuppied("Hay una pieza que bloquea el camino")
              
        #Code below sets the piece in the new position and errase the old one, after that it changes the turn
        self.__board__.set_piece(None, from_row, from_col)
        self.__board__.set_piece(piece, to_row, to_col)
        self.change_turn()
        

    def change_turn(self): #This method changes the turn, it is used to change the turn after a move
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def show_board(self): #This method calls show_board from the board class and returns the board representation, used in cli.py
        return self.__board__.show_board()

    def is_playing(self):
        return self.__playing__
    
    def end_game(self): #This method ends the game, it is used in cli.py and in king_dead method below
        self.__playing__ = False

    #This method checks if the king is dead, and if it is, it ends the game
    def king_dead(self, to_row, to_col):
        #Verifies if the piece captured is a king
        target_piece_king = self.target_piece(to_row, to_col)
        if isinstance(target_piece_king, King):
            #If the king is dead, it ends the game
            self.end_game()
            
            #Get the color of the king captured and the winning color, to print the text
            king_color = target_piece_king.get_color()
            winning_color = "BLACK" if king_color == "WHITE" else "WHITE"
            
            #Prints the winning message
            print(f"¡El rey {king_color} ha sido capturado! ¡{winning_color} gana la partida!")
            return True
        return False