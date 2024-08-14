
from chess import Chess
def main():
    chess = Chess()
    try:
        from_row = int(input('From row: '))
        from_col = int(input('From row: '))
        to_row = int(input('To row: '))
        to_col = int(input('To row: '))

        chess.move(
        from_row,
        from_col,
        to_row,
        to_col,
    )
    
    except Exception as e:
            print("error")


if __name__ == '__main__':
    main()