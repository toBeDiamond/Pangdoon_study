T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 1, 1, 0, -1, -1, -1]            # 8 방향으로 총을 쏜다.
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    count = 0     # 죽는 토끼 마리 수
    for i in range(N):      # 총을 쏠 사냥꾼 찾기
        for j in range(N):
            if arr[i][j] == 1:    # 사냥꾼 위치 지정
                for k in range(8):              # 총 8 방향으로 쏘기
                    for m in range(1, N):            # 총이 닿는 범위
                        ni = i + di[k] * m          # 사냥꾼 위치 지정한 곳에서 총을 쏜다.
                        nj = j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N:     # 총이 닿을 수 없는 최대 범위 설정해주기
                            if arr[ni][nj] == 2:
                                count += 1                  # 총으로 죽인 토끼들 마리 세어주기
                            elif arr[ni][nj] == 1:                   # 사냥꾼이 라면?
                                break                       # 총쏘지마세요.
                            elif arr[ni][nj] == 3:                   # 바위라면?
                                break                       # 총쏘지마세요.

    print(f'#{test_case} {count}')                          # 전체 합으로 더해주기