T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_count = 0
    for i in range(N):
        for j in range(M):
            count = arr[i][j]
            for k in range(4):
                    if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
                        count += arr[i + di[k]][j + dj[k]]
                        if count > max_count:
                            max_count = count

    print(f'#{test_case} {max_count}')