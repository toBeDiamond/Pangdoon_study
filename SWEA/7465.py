def dfs(v):
    global count
    for i in muri[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    muri = [[] for _ in range(N+1)]  
    visited = [0] * (N+1)
    count = 0
    for i in range(M):
        a, b = map(int, input().split())
        muri[a].append(b)
        muri[b].append(a)
    for k in range(1, N+1):
        if visited[k] == 0:
            count += 1
            visited[k] = 1
            dfs(k)

    print(f'#{test_case} {count}')


