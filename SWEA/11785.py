T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[0]
    min_value = arr[0]

    for i in range(N):
        if arr[i] > max_value:
            max_value = arr[i]

        if arr[i] < min_value:
            min_value = arr[i]

    ans = max_value - min_value

    print(f'#{tc} {ans}')