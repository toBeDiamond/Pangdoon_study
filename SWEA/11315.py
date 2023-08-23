T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [0, 1, 1, 1]       # 오른쪽, 오른쪽 밑 대각선, 아래, 왼쪽 밑 대각선
    dj = [1, 1, 0, -1]      # 8방향까지 안보고 4방향만 봐도 오목인지 확인가능

    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    count = 1
                    for m in range(1, 5):
                        ni = i + di[k] * m
                        nj = j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                count += 1
                            else:
                                break
                    if count == 5:
                        flag = 1
    print(f'#{test_case}', end=' ')
    if flag:
        print('YES')
    else:
        print('NO')

