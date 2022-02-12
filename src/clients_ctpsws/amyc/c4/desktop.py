import connectfour

RED = connectfour.RED
YELLOW = connectfour.YELLOW
EMPTY = connectfour.EMPTY


def main():
    size_of_board = (4, 8)  # cols, ros
    turn = RED
    game = connectfour.new_game(size_of_board[0], size_of_board[1])
    while True:
        print(game.turn)
        # transposed = list(zip(*game.board))
        for row in game:
            print(row)
        while True:
            move_col = int(input("Enter your move (column): ")) -1
            drop_or_pop = input("Enter drop or pop: ")
            if not (0 <= move_col <= size_of_board[0] - 1):
                print(f"Column must be between 1 & {size_of_board[0]}")
                continue
            if drop_or_pop not in ("drop", "pop"):
                print("Must enter drop or pop")
                continue
            break
        if drop_or_pop == "drop":
            game = connectfour.drop(game, move_col)
        else:
            game = connectfour.pop(game, move_col)
        if turn == RED:
            turn = YELLOW
        else:
            turn = RED


if __name__ == "__main__":
    main()
