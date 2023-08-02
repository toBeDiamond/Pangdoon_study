T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    for i in range(N):
        if max_value < arr[i]:
            max_value = arr[i]


        if min_value > arr[i]:
            min_value = arr[i]

    ans = max_value - min_value

    print(f'#{test_case} {ans}')