T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    super_total = 0
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(M):
                for p in range(M):
                    if 0 <= i + k < N and 0 <= j + p < N:
                        total += arr[i + k][j + p]
                        if super_total < total:
                            super_total = total
    
    print(f'{test_case} {super_total}')