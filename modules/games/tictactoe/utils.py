WIN_PATTERNS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def check_winner(board):
    for pattern in WIN_PATTERNS:
        a, b, c = pattern

        if (
            board[a] != ""
            and board[a] == board[b]
            and board[a] == board[c]
        ):
            return board[a]

    return None


def check_tie(board):
    return all(cell != "" for cell in board)