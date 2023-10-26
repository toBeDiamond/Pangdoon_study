from collections import deque

def bfs(v):
    visited = [0] * (N + 1)
    global cnt
    while Q:
        tmp = Q.popleft()
        visited[v] = 1
        for k in graph[tmp]:
            if visited[k] == 0:
                visited[k] = 1
                Q.append(k)
                cnt += 1


N, M = map(int, input().split())


count = [0] * (N+1)
graph = [[] for _ in range(N+1)]

Q = deque()
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(N+1):
    cnt = 1
    Q.append(i)
    bfs(i)
    count[i] = cnt

result = []
for i in range(1, N+1):
    if count[i] == max(count):
        result.append(i)
print(*sorted(result))
