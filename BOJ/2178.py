from collections import deque

N, M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]
miro = [[0] * M for _ in range(N)]
Q = deque()
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
Q.append((0, 0))
miro[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        ni = tmp[0] + di[i]
        nj = tmp[1] + dj[i]
        if 0 <= ni < N and 0 <= nj <M and board[ni][nj] == 1:
            board[ni][nj] = 2
            miro[ni][nj] = miro[tmp[0]][tmp[1]] + 1
            Q.append((ni, nj))

print(miro[N-1][M-1])