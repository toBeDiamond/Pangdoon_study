from collections import deque

T = int(input())

for test_case in range(T):
    M, N, K = map(int, input().split())
    baechu = [[0] * M for _ in range(N)]
    Q = deque()
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    count = 0
    for _ in range(K):
        a, b = map(int, input().split())
        baechu[b][a] = 1

    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                Q.append((i, j))
                count += 1
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        ni = tmp[0] + di[k]
                        nj = tmp[1] + dj[k]
                        if 0 <= ni < N and 0 <= nj < M and baechu[ni][nj] == 1:
                            baechu[ni][nj] = 2
                            Q.append((ni, nj))
    print(count)

