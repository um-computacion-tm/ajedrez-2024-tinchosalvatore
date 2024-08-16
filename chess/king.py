from pieces import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, move):
        ...