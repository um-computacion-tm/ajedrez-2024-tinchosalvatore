# Excepciones de movimientos invalidos
class InvalidMove(Exception):
    pass

class InvalidMoveNoPiece(InvalidMove):
    ...

class InvalidMoveSameColor(InvalidMove):
    ...

class InvalidMovePieceFromOtherColor(InvalidMove):
    ...