def dfs(v):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    visited = [0] * (N+1)
    adj_list = [[] for _ in range(N+1)]    # 인접리스트 초기화

    # 인접리스트를 만들기
    for i in range(M):
        s, e = temp[2*i], temp[2*i+1]
        adj_list[s].append(e)
        adj_list[e].append(s)

    count = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            count += 1
    print(f'#{test_case} {count}')