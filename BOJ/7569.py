from collections import deque

Q = deque()
di = [0, 1, 0, -1, 0, 0]
dj = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
X, Y, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(H)]
dis = [[[0] * X for _ in range(Y)] for _ in range(H)]


for i in range(H):
    for j in range(Y):
        for k in range(X):
            if board[i][j][k] == 1:
                Q.append((i, j, k))

while Q:
    tmp = Q.popleft()
    for i in range(6):
        ni = tmp[0] + di[i]
        nj = tmp[1] + dj[i]
        nz = tmp[2] + dz[i]
        if 0 <= ni < H and 0 <= nj < Y and 0 <= nz < X and board[ni][nj][nz] == 0:
            board[ni][nj][nz] = 1
            dis[ni][nj][nz] = dis[tmp[0]][tmp[1]][tmp[2]] + 1
            Q.append((ni, nj, nz))
flag = 1
for i in range(H):
    for j in range(Y):
        for k in range(X):
            if board[i][j][k] == 0:
                flag = 0
                break

result = 0
if flag == 1:
    for i in range(H):
        for j in range(Y):
            for k in range(X):
                if result < dis[i][j][k]:
                    result = dis[i][j][k]
    print(result)
else:
    print(-1)