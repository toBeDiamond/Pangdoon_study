T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            M = 0
            if arr[i][j] == 'A':
                M = 1
            elif arr[i][j] == 'B':
                M = 2
            elif arr[i][j] == 'C':
                M = 3
            for k in range(4):
                for w in range(1, M+1):
                    ni = i + di[k] * w
                    nj = j + dj[k] * w
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count += 1

    print(f'#{test_case} {count}')









