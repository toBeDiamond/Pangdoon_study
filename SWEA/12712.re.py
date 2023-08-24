T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dii = [-1, 1, 1, -1]
    djj = [1, 1, -1, -1]


    super_max = 0    # 좌우사방향
    for i in range(N):
        for j in range(N):
            max_value = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        max_value += arr[ni][nj]
            if max_value > super_max:
                super_max = max_value

    for i in range(N):
        for j in range(N):
            max_value2 = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + dii[k] * m
                    nj = j + djj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        max_value2 += arr[ni][nj]
            if max_value2 > super_max:
                super_max = max_value2

    print(f'#{test_case} {super_max}')