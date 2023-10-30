from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))

    index = 0
    Q = deque()
    for i in P:
        Q.append((i, index))
        index += 1
    count = 0

    while Q:
        tmp = Q.popleft()
        if tmp[0] == max(P):
            count += 1
            P.remove(max(P))
            if tmp[1] == M:
                break
        else:
            Q.append(tmp)

    print(count)





