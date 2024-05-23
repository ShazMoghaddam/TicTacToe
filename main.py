def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'x'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row number (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column number (0, 1, 2): "))

        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'o' if current_player == 'x' else 'x'


tic_tac_toe()