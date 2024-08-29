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

class InvalidMoveRook(InvalidMove):
    ...

class InvalidMoveKnight(InvalidMove):
    ...

class InvalidMoveBishop(InvalidMove):
    ...

class InvalidMoveQueen(InvalidMove):
    ...

class InvalidMoveKing(InvalidMove):
    ...

class InvalidMovePawn(InvalidMove):
    ...
