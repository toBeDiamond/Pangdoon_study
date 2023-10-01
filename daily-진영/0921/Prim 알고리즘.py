'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# import heapq
#
# def prim(start):
#     heap = []
#     # MST 에 포함되었는 지 여부
#     MST = [0] * V
#
#     # 가중치, 정점 정보
#     heapq.heappush(heap, (0, start))
#     # 누적합 저장
#     sum_weight = 0
#
#     while heap:
#         # 가장 적은 가중치를 가진 정점을 꺼냄
#         weight, v = heapq.heappop(heap)
#
#         # 이미 방문한 노드라면 pass
#         if MST[v]:
#             continue
#
#         # 방문 체크
#         MST[v] = 1
#
#         # 누적합 추가
#         sum_weight += weight
#
#
#         # 갈 수 있는 노드들을 체크
#         for next in range(V):
#             # 갈 수 없거나 이미 방문했다면 pass
#             if graph[v][next] == 0 or MST[next]:
#                 continue
#
#             heapq.heappush(heap, (graph[v][next], next))
#     return sum_weight
#
#
# V, E = map(int, input().split())
# # 인접행렬
# graph = [[0] * V for _ in range(V)]
#
# for _ in range(E):
#     f, t, w = map(int, input().split())
#     graph[f][t] = w
#     graph[t][f] = w       # 무방향 그래프이므로 양방향으로 넣어주어야 한다.(대각선으로 대칭)
#
# result = prim(0)
# print(f'최소 비용 = {result}')

def prim(s):
    total = 0
    # 시작점 설정
    D[s] = 0
    # 정점의 개수만큼 선택하기
    for i in range(V + 1):
        # 1. 가중치 최소값 찾기
        min_v = 987654321
        for j in range(V + 1):
            if visited[j] == 0 and min_v > D[j]:
                min_v = D[j]
                v = j  # 가중치 최소인 정점 선택
        # 2. 방문처리 (선택)
        visited[v] = 1
        total += adj_m[PI[v]][v]
        # 3. 인접 정점의 부모, 가중치 갱신
        for w in range(V + 1):
            if adj_m[v][w] and not visited[w]:
                if D[w] > adj_m[v][w]:
                    D[w] = adj_m[v][w]  # 가중치 갱신
                    PI[w] = v  # 부모 갱신

    return total


V, E = map(int, input().split())  # 0부터 마지막 정점 수, 간선 수
adj_m = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬
visited = [0] * (V + 1)  # 방문체크
D = [987654321] * (V + 1)  # 가중치
PI = list(range(V + 1))  # 부모 (초기에는 본인)

# 인접행렬 만들기
for i in range(E):
    s, e, w = map(int, input().split())  # start, end, weight
    adj_m[s][e] = adj_m[e][s] = w

print(prim(0))  # 가중치의 합
