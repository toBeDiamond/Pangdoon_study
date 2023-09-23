def dijkstra(s):
    # 시작점 설정
    D[s] = 0
    # 정점의 개수만큼 선택하기
    for i in range(V+1):
        # 가중치 최소값 찾기
        min_v = 987654321
        for j in range(V+1):
            if visited[j] == 0 and min_v > D[j]:
                min_v = D[j]
                v = j                       # 가중치 최소인 정점 선택
        # 방문처리 (선택)
        visited[v] = 1
        # 인접 정점의 부모, 가중치 갱신
        for w in range(V+1):
            if adj_m[v][w] and not visited[w]:
                if D[w] > D[v] + adj_m[v][w]:
                    D[w] = D[v] + adj_m[v][w]   # 가중치 갱신

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    # 0부터 마지막 정점 수, 간선 수
    adj_m = [[0] * (V+1) for _ in range(V+1)]   # 인접행렬
    visited = [0] * (V+1)                       # 방문체크
    D = [987654321] * (V+1)                     # 가중치
    # 인접행렬 만들기
    for i in range(E):
        s, e, w = map(int, input().split())     # start, end, weight
        adj_m[s][e] = w
    dijkstra(0)
    result = D[V]
    print(f'#{test_case} {result}')