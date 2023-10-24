import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt

    visited[v] = 1
    for k in graph[v]:
        if visited[k] == 0:
            visited[k] = 1
            cnt += 1
            dfs(k)
            visited[k] = 0


N, M = map(int, input().split())


count = [0] * (N+1)
graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(N+1):
    cnt = 1
    dfs(i)
    count[i] = cnt

result = []
for i in range(1, N+1):
    if count[i] == max(count):
        result.append(i)
print(*sorted(result))
