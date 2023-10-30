import sys
sys.setrecursionlimit(10**6)


N = int(input())

arr = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0] * (N+1)
visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    for child in arr[node]:
        if not visited[child]:
            answer[child] = node
            dfs(child)

# 트리의 루트를 찾기 위해 어떤 노드를 시작점으로 설정해도 됩니다.
# 여기서는 1번 노드를 시작점으로 설정합니다.
dfs(1)

# 2번 노드부터 N번 노드까지 각 노드의 부모를 출력
for i in range(2, N+1):
    print(answer[i])