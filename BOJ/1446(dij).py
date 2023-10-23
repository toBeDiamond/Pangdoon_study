import heapq

N, D = map(int, input().split())  # D : 고속도로의 길이
# 인접리스트
graph = [[] for _ in range(D + 1)]  # 고속도로의 길이에 맞게 인덱스 값을 설정해준다 ( 0부터 150까지 )

for i in range(D):     # 우선 고속도로의 길이(지름길 없이) 만큼 가중치를 넣어준다. 예를들어 1, 1 / 2, 2 / 3, 3 /
                       # 150 고속도로를 가는데 1km 움직이면 1km 움직인 것, 2km 까지 움직이면 2km 까지 움직인 것 (지름길 X)
    graph[i].append((i + 1, 1))  # 도착점, 가중치를 설정해준다, 가중치는 기본 1로!!

for i in range(N):     # 지름길 있는 것을 더 첨가해서 넣어준다.
    s, e, length = map(int, input().split())    # 지름길 시작점, 지름길 끝나는점, 지름길의 길이를 넣어준다.
    if e <= D:    # 하지만 지름길이 끝나는 점이 고속도로 전체의 길이를 넘는다면 애시당초 넣어주지 않는다.
        graph[s].append((e, length))  # 시작점에 어디까지 가는지, 지름길을 넣어준다.

INF = 987654321    # 큰 값으로 모든 거리를 나타내어 준다. (최소 거리 찾기 위해서 )
dist = [INF] * (D + 1)

# 초기화
Q = []    # 빈 Q를 만들어준다.
heapq.heappush(Q, (0, 0))   # heapq의 사용법은 push 할때 (Q, (넣을 것)) 이다. 시작은 0이고, 가중치도 0이므로 넣어준다.
dist[0] = 0   # 거리를 나타내주는 인덱스에 0(시작점)은 0만큼 간것이므로 넣어준다.

while Q:
    now_dist, now = heapq.heappop(Q)    # (0, 0) 으로 시작한 것에서 now_dist 가중치 0, 현재 위치 0 (시작점)을 빼준다.
    # if dist[now] < d: continue

    for next, length in graph[now]:    # 0번째에서 다음으로 갈 곳을 for 문을 통해 간다, 그에 따른 가중치는 length
        cost = now_dist + length    # 그렇게 나온 다음 가중치를 cost 로 두고 현재까지의 거리 + next 까지 온 거리에 대한 거리를 더해준다.

        if dist[next] > cost:    # 만약에 다음으로 온 거리보다 현재 방법으로 온 거리가 더 짧다면
            dist[next] = cost    # 거리를 더 조금걸린 것으로 갱신해준다.
            heapq.heappush(Q, (dist[next], next))  # 그리고 그것을 다시 넣어준다. (다음 곳을 방문해야하기 때문에)
            # 이와 같은 것을 계속 반복한다면 distance 에는 그 인덱스, 그 고속도로 거리만큼 가기위해 필요한 최소한의 거리를 알려주게 된다.

print(dist[D])   # 고속도로 전부달린 D값을 구해야하므로 dist[D]를 적어주면 답이 나온다.
