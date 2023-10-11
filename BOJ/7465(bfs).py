from collections import deque
def bfs(v):
    while Q:
        tmp = Q.popleft()
        if visited[tmp] == 0:
            visited[tmp] = 1
            for i in muri[tmp]:
                if visited[i] == 0:
                    Q.append(i)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    muri = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    count = 0
    Q = deque()
    for i in range(M):
        a, b = map(int, input().split())
        muri[a].append(b)
        muri[b].append(a)
    for k in range(1, N+1):
        if visited[k] == 0:
            Q.append(k)
            count += 1
            bfs(k)

    print(f'#{test_case} {count}')