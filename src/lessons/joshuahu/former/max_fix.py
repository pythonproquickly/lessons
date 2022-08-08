def max_value(board):
    optimal_move = None
    v = float("-inf")
    if terminal(board):
        info = (utility(board), None)
        return info
    else:
        for move in actions(board):
            new_value = min_value(result(board, move))[0]
            if new_value is None:
                print("F")
                break
            if v < new_value:
                v = new_value
                optimal_move = move
        info = (v, optimal_move)
        return info
