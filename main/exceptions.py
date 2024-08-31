# Excepciones de movimientos invalidos

class InvalidInput(Exception):
    pass

class InvalidMove(Exception):
    pass

class InvalidMoveNoPiece(InvalidMove):
    ...

class InvalidMoveSameColor(InvalidMove):
    ...

class InvalidMovePieceFromOtherColor(InvalidMove):
    ...

class InvalidMoveNotInBoard(InvalidMove):
    ...

class InvalidMovePathOcuppied(InvalidMove):
    ...

class InvalidMoveVerticalHorizontal(InvalidMove):
    ...

class InvalidMoveDiagonal(InvalidMove):
    ...

class InvalidMoveNotAllowed(InvalidMove):
    ...

class InvalidMoveKnight(InvalidMove):
    ...

class InvalidMovePawn(InvalidMove):
    ...