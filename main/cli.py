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

        from_row_input = input("Desde fila: ").strip().lower()
        if from_row_input == "exit":
            chess.end_game()  # Asegúrate de tener un método para terminar el juego
            return
        
        try:
            from_row = int(from_row_input)
        except ValueError:
            raise InvalidInput("Ingrese numeros para jugar o exit para termianar el juego.")
        
        try:
            from_col = int(input("Desde col: "))
            to_row = int(input("A la fila: "))
            to_col = int(input("A la col: "))
        except ValueError:
            raise InvalidInput("Ingrese numeros")
        

        chess.move_piece(from_row, from_col, to_row, to_col)
    
    except InvalidMove as e:
        print("Movimiento invalido: ", e)

    except InvalidInput as e:    
        print("Entrada inválida: ", e)
        
    except Exception as e:
        print("Sucedio un error inesperado", e) 


if __name__ == '__main__':
    main()