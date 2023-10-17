from collections import deque

Y, X = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(X)]
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
Q = deque()
dis = [[0] * Y for _ in range(X)]

for i in range(X):
    for j in range(Y):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    temp = Q.popleft()
    for i in range(4):
        ni = temp[0] + di[i]
        nj = temp[1] + dj[i]
        if 0 <= ni < X and 0 <= nj < Y and board[ni][nj] == 0:
            board[ni][nj] = 1
            dis[ni][nj] = dis[temp[0]][temp[1]] + 1
            Q.append((ni,nj))

flag = 1
for i in range(X):
    for j in range(Y):
        if board[i][j] == 0:
            flag = 0
            break
result = 0
if flag == 1:
    for i in range(X):
        for j in range(Y):
            if result < dis[i][j]:
                result = dis[i][j]
    print(result)
else:
    print(-1)