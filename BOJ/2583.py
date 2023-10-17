import sys
sys.setrecursionlimit(10**6)

def dfs(a, b, c):
    board[a][b] = 1
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 0:
            c = dfs(ni, nj, c+1)
    return c

M, N, K = map(int, input().split())
result = []
count = 0
board = [[0] * N for _ in range(M)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            count += 1
            result.append(dfs(i, j, 1))
result.sort()
print(count)
print(*result)




