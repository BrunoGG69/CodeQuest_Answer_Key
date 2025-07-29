def chk(board):
    for i in board:
        if not set([1, 2, 3, 4]).issubset(i):
            return 0
    return 1

def verify(x, y, board, num):
    for i in range(4):
        if board[x][i % 4] == num or board[i % 4][y] == num:
            return 0
    sr = x - (x % 2)
    sc = y - (y % 2)

    for i in range(2):
        for j in range(2):
            if board[i + sr][j + sc] == num:
                return 0

    return 1

def solver(board, x, y):
    if x == 3 and y == 4:
        return board
    if y == 4:
        x += 1
        y = 0

    if board[x][y] != 0:
        return solver(board, x, y + 1)

    for i in range(1, 5):
        if verify(x, y, board, i):
            board[x][y] = i
            solver(board, x, y + 1)

    return board

def solve(board):
    board = solver(board, 0, 0)
    if not chk(board):
        return 0
    return board
board = eval(input())

print(solve(board))
