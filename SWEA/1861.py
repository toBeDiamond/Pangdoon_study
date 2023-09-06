
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    min_start = 0
    max_count = 0
    for i in range(N):
        for j in range(N):
            p = i
            q = j
            count = 1
            start = room[i][j]
            while True:
                for k in range(4):
                    ni = p + di[k]
                    nj = q + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[p][q] + 1:
                        p = ni
                        q = nj
                        count += 1
                        break
                else:
                    break
            if max_count < count:
                max_count = count
                min_start = start
            elif max_count == count and min_start > start:
                min_start = start

    print(f'#{test_case} {min_start} {max_count}')