import heapq, sys                                      # heapq 와 sys를 불러온다.

V, E = map(int, sys.stdin.readline().split())          # 빠르게 input 해주기.
K = int(input())
graph = [[] for _ in range(V+1)]                       # 인접리스트 만들어주기
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])                            # 인접리스트 단방향으로 가중치와 같이 값 넘겨주기

INF = int(1e9)
distance = [INF] * (V+1)                               # 거리값을 나타내줄 큰값으로 구성된 것 만들어주기 (인덱스 0을 안쓰므로 + 1)

def dijkstra(start):                                   # 다익스트라 시작합니다.
    pq = []                                            # 빈 리스트 만들어주기.
    heapq.heappush(pq, (0, start))                     # pq 리스트에다가 넣어줍니다. 0 가중치, start 시작점
    distance[start] = 0                                # 처음 들어간 곳은 거리가 0이므로 0으로 바꾸어 줍니다.

    while pq:
        dist, now = heapq.heappop(pq)                 # pq를 빼주면 dist, now / 거리에 대한 가중치와 시작한 지점이 나옵니다.
        if distance[now] < dist:                      # 이미 방문한 지점이 방금 꺼낸 누적 거리의 값보다 더 작다면 PASS
            continue

        for next in graph[now]:                       # 다음 노드로 움직일 next_node 값 찾아주기
            next_node = next[0]                       # [v(다음 노드), w(가중치)]로 구성되어있으므로 next_node 는 인덱스 0
            cost = next[1]                            # 가중치는 인덱스 1
            new_cost = dist + cost                    # 갱신된 가중치는 dist + cost

            if distance[next_node] <= new_cost:       # 만약 방문한 곳의 가중치가 새로 갱신된 가중치보다 작다면
                continue                              # PASS

            distance[next_node] = new_cost                  # 아니라면 새로운 가중치로 갱신해준다.
            heapq.heappush(pq, (new_cost, next_node))       # pq 에 가중치와, 다음 방문지를 넣어준다

dijkstra(K)
for i in range(1, V+1):                              # index 0 은 애시당초 10000000으로 큰값으로 나타나있고 무쓸모한 값이므로 1부터
    if distance[i] == INF:                           # 만약 거리가 이미 설정해줬떤 INF 값이면 닿지않는 곳이므로 INF 출력
        print('INF')
    else:
        print(distance[i])                           # 각 인덱스별로 얼마나 거리가 있는지 출력


