def work_percent(N, K, percent):    # N은 고를 것의 개수, K는 X번째사람이 고를 것, percent는 곱한것의 합계
    global result
    if result >= percent:
        return

    if N == K:
        if result < percent:
            result = percent
        return               # N == K 가 같으면 이 함수는 끝이난다.

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            work_percent(N, K+1, percent * work[K][i] / 100)
            visited[i] = 0



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    work_percent(N, 0, 1)

    print(f'#{test_case} {result * 100:0.6f}')