def find_page(page, key):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        cnt += 1
        if middle == key:
            return cnt

        elif middle > key:
            end = middle

        else:
            start = middle

    return -1

T = int(input())
for test_case in range(1, T+1):
    p, a, b = map(int,input().split())
    a1 = find_page(p, a)
    b1 = find_page(p, b)
    if a1 == b1:
        ans = 0
    elif a1 > b1:
        ans = "B"
    else:
        ans = "A"

    print(f'#{test_case} {ans}')
