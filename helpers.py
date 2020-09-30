def win(board):
    # Row win
    for row in board:
        if row[0] != None and row[0] == row[1] == row[2]:
            return True

    # Column win
    for col in range(3):
        if board[0][col] != None and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Diagonal win A
    if board[0][0] != None and board[0][0] == board[1][1] == board[2][2]:
        return True

    # Diagonal win B
    if board[0][2] != None and board[0][2] == board[1][1] == board[2][0]:
        return True

    # There is no winner
    return False
    
def tie(board):
    # There will be a tie if all moves are made without a win
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                return False
    return True
