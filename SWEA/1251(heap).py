import heapq

def prim(start):
    total = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        d, v = heapq.heappop(heap)
        if visited[v] == 0:
            visited[v] = 1
            total += d
            for w in range(V):
                if visited[w] == 0 and weight[w] > arr[v][w]:
                    weight[w] = arr[v][w]
                    heapq.heappush(heap, (weight[w], w))
    return total * S

T = int(input())

for test_case in range(1, T + 1):
    V = int(input())
    weight = [2e12] * V
    visited = [0] * V
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    S = float(input())
    arr = [[0] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            arr[i][j] = arr[j][i] = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)

    print(f'#{test_case} {round(prim(0))}')