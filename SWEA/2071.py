T = int(input())


for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    total = 0
    count = 0
    for i in range(10):
        total += arr[i]
        count += 1

    ans = total / count
    print(f'#{test_case} {ans:.0f}')
