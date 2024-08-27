from main.chess import Chess
from main.exceptions import *

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn())
        from_row = int(input("Desde fila: "))
        from_col = int(input("Desde col: "))
        to_row = int(input("A la fila: "))
        to_col = int(input("A la col: "))
        # :)
        chess.move(from_row, from_col, to_row, to_col)
    
    except InvalidMove as e:
        print("Movimiento invalido: ", e)
    except Exception as e:
        print("Sucedio un error inesperado", e) 


if __name__ == '__main__':
    main()