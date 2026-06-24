def game(board):
    r, c = len(board), len(board[0])
    new = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            live = 0
            for x in range(max(0,i-1), min(r,i+2)):
                for y in range(max(0,j-1), min(c,j+2)):
                    live += board[x][y]

            live -= board[i][j]

            if live == 3 or (board[i][j] == 1 and live == 2):
                new[i][j] = 1

    return new

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(game(board))
