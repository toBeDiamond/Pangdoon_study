import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = 1
    for k in board[v]:
        if visited[k] == 0:
            dfs(k)

N, M = map(int, sys.stdin.readline().split())
result = 0
board = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)