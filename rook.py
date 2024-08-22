from pieces import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
 
    def is_valid_move(self, move):
        from_row, from_col = self.__position__
        to_row, to_col = move

        # Verifica que la torre se mueva en linea horizontal o vertical
        if from_row != to_row and from_col != to_col:
                return False
        
        # Movimiento horizontal
        if from_row == to_row:  
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                 return True
                 
        elif from_col == to_col:  # Movimiento vertical
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):                 
                return True