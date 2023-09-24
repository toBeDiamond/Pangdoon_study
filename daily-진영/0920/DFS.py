# 인접행렬
# 장점 : 구현이 쉽다.
# 단점 : 메모리 낭비
#       0 도 표시하기 때문에


# stack 버전
#DFS
def dfs_stack(start):

    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack 에 추가
        for next in range(4, -1, -1):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 stack 에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]
print("dfs stack = ", end='')
print(*dfs_stack(0))



# 재귀

visited =[0] * 5
path = []

def dfs(now):
    visited[now] = 1
    print(now, end= ' ')

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue

        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end = ' ')
dfs(0)

