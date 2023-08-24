def check(tmp):
    txt = list(str(tmp))
    for i in range(len(txt)-1):
        if txt[i] > txt[i+1]:
            return False

    return True

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = []
    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = arr[i] * arr[j]
            if check(tmp):
                if ans < tmp:
                    ans = tmp

    print(f'#{test_case} {ans}')