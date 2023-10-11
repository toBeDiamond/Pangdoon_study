from collections import deque

def bfs(v):
    global count
    while Q:
        tmp = Q.popleft()
        for k in range(8):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if 0 <= ni < Y and 0 <= nj < X and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                Q.append((ni, nj))


while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(Y)]
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    Q = deque()
    count = 0
    visited = [[0] * X for _ in range(Y)]
    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 1:
                visited[i][j] = 1
                Q.append((i,j))
                bfs((i,j))
                count += 1
    print(count)

