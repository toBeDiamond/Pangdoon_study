from collections import deque

def dfs(V):
    dfs_list.append(V)
    visited[V] = 1
    for i in sorted(arr[V]):  # 현재 정점 V와 연결된 정점을 정렬해서 방문
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

def bfs(V):
    visited2[V] = 1
    while Q:
        tmp = Q.popleft()
        bfs_list.append(tmp)
        for k in sorted(arr[tmp]):  # 현재 정점 tmp와 연결된 정점을 정렬해서 방문
            if visited2[k] == 0:
                Q.append(k)
                visited2[k] = 1

N, M, V = map(int, input().split())
visited = [0] * (N + 1)
Q = deque()
arr = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs_list = []
bfs_list = []

dfs(V)
Q.append(V)
visited2 = [0] * (N + 1)
bfs(V)

print(*dfs_list)
print(*bfs_list)