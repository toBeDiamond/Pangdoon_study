N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    count = 0
    for m in range(i-1, x):
        for n in range(j-1, y):
            count += arr[m][n]
    print(count)
