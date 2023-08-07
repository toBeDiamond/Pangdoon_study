T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    si = [1, 1, -1, -1]
    sj = [-1, 1, 1, -1]
    super_total = 0
    for i in range(N):   # 십자형으로 스프레이를 뿌렸을 때
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for m in range(1, M): # M 값을 무엇으로 주어야 할지 모르겠어요 센세
                    if 0 <= i + di[k]*m < N and 0 <= j + dj[k]*m < N:
                        total += arr[i + di[k] * m][j + dj[k] * m]
                        if super_total < total:
                            super_total = total


    super_count = 0    # 대각선으로 스프레이를 뿌렸을 때
    for i in range(N):  # 십자형으로 스프레이를 뿌렸을 때
        for j in range(N):
            count = arr[i][j]
            for k in range(4):
                for m in range(1, M):  # M 값을 무엇으로 주어야 할지 모르겠어요 센세
                    if 0 <= i + si[k] * m < N and 0 <= j + sj[k] * m < N:
                        count += arr[i + si[k] * m][j + sj[k] * m]
                        if super_count < count:
                            super_count = count

    if super_total > super_count:
        ans = super_total

    elif super_total < super_count:
        ans = super_count

    else:
        ans = super_total

    print(f'#{test_case} {ans}')