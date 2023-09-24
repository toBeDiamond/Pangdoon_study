def perm(N, k, s):

    global result
    if s >= result:
        return

    if N == k:        # N == k이면 함수종료
        if s <= result:
            result = s

        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(N, k+1, arr[k][i] + s)
                visited[i] = 0

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 987654321
    perm(N, 0, 0)
    print(f'#{test_case} {result}')
