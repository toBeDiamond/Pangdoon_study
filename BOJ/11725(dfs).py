import sys
sys.setrecursionlimit(10**6)


N = int(input())

arr = [[] for _ in range(N+1)]                      # 빈 인접리스트

for i in range(N-1):                                # 양방향 인접리스트 만들어 주기
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0] * (N+1)
visited = [0] * (N+1)                           # visited 체크해주기

def dfs(node):                                      # dfs, 시작 node는 항상 1
    visited[node] = 1                               # visited 체크해주기
    for child in arr[node]:                         # 인접리스트를 가지고 그 정점과 연결된 노드 꺼내기
        if visited[child] == 0:                     # visited 체크가 안되어있는 연결된 노드라면
            answer[child] = node                    # 그 인덱스에 부모노드 넣어주기
            dfs(child)

# 트리의 루트를 찾기 위해 어떤 노드를 시작점으로 설정해도 됩니다.
# 여기서는 1번 노드를 시작점으로 설정합니다.
dfs(1)

# 2번 노드부터 N번 노드까지 각 노드의 부모를 출력
for i in range(2, N+1):
    print(answer[i])