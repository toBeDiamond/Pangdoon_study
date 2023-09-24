def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        edge.append([n1, n2, w])
    # 가중치를 기준으로 정렬해준다.
    edge.sort(key=lambda x: x[2])
    # 사이클의 발생 여부를 union find로 찾아낸다.
    parents = [i for i in range(V+1)]

    count = 0
    sum_weight = 0
    for n1, n2, w in edge:
        # 싸이클이 발생하지 않는다면
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            sum_weight += w
            count += 1

            # 최소 신장트리는 노드 - 1개의 간선개수를 가짐
            if count == V:
                break
    print(f'#{test_case} {sum_weight}')




