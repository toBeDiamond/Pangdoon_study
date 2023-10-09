import sys

sys.setrecursionlimit(10**6)

def dfs(x, y, h):
    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0 and area[ni][nj] > h:
            board[ni][nj] = 1
            dfs(ni, nj, h)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

result = 0
for h in range(100):
    cnt = 0
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] > h and board[i][j] == 0:
                board[i][j] = 1
                dfs(i, j, h)
                cnt += 1
    if cnt > result:
        result = cnt
    if cnt == 0:
        break

print(result)
