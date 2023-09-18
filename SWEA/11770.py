def hoare_partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1  # 왼쪽에서 큰값
        while i <= j and a[j] >= p:
            j -= 1  # 오른쪽에서 작은값
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]   # 피봇과 j의 값을 교환
    return j   # 피봇자리


def quick_sort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)
        # pivot = lomuto_partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{test_case} {arr[N//2]}')
