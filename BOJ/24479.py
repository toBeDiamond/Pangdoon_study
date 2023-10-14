import sys
sys.setrecursionlimit(10**6)

def dfs(v, n):
    visited[v] = n
    for k in sorted(board[v]):
        if visited[k] == 0:
           n = dfs(k, n+1)
    return n

N, M, R = map(int, sys.stdin.readline().split())

board = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)


dfs(R, 1)
for i in range(1, N+1):
    print(visited[i])
