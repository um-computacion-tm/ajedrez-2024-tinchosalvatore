import os 
from main.chess import Chess
from main.exceptions import *

def clear_screen(): #This method clears the screen after every move
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def validate_position(value): #This method validates the value of the input
    if not (0 <= value <= 7):
        raise InvalidInput("Las posiciones deben estar entre 0 y 7.") #raises an exception if the value exceeds the range

def play(chess):
    
    try:
        print("Ingrese exit en la primera fila para terminar el juego") 
        print(chess.show_board())
        print("turn: ", chess.turn())

        from_row_input = input("Desde fila: ").strip().lower()
        if from_row_input == "exit":
            chess.end_game()  #Ends the game in case that the User typed exit
            print("El usuario terminó el juego.")
            return
        
        try:
            from_row = int(from_row_input)
            validate_position(from_row) #Validates the input
        except ValueError:
            raise InvalidInput("Ingrese numeros para jugar o exit para termianar el juego.") #Exception in case the input is not a number
        
        try:
            from_col = int(input("Desde col: "))
            validate_position(from_row)
            to_row = int(input("A la fila: "))
            validate_position(from_row)            
            to_col = int(input("A la col: "))
            validate_position(from_row)
        except ValueError:
            raise InvalidInput("Ingrese numeros")
        

        chess.move_piece(from_row, from_col, to_row, to_col)

    except InvalidMove as e:
        print("Movimiento invalido: ", e) #Invalid move exceptions are printed here

    except InvalidInput as e:    
        print("Entrada inválida: ", e) #Invalid input exceptions are printed here

if __name__ == '__main__':
    main()