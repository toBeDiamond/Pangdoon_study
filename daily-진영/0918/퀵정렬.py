def lomuto_partition(arr, left, right):
    # 맨 오른쪽 요소를 pivot 으로 설정하고
    # i = left -1
    # j = left
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        # arr[j]가 pivot보다 작으면,
        if arr[j] < pivot:
            # i를 증가,
            # arr[j], arr[i] 위치교환
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # i가 가리키는 위치가 pivot보다 작은값의 마지막 인덱스
    # i+1 의 위치에 pivot을 두고 i+1 반환
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


def hoare_partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p: i += 1  # 왼쪽에서 큰값
        while i <= j and a[j] >= p: j -= 1  # 오른쪽에서 작은값
        if i < j : a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]   # 피봇과 j의 값을 교환
    return j   # 피봇자리


def quick_sort(a, l, r):
    print(arr)
    if l < r:
        # pivot = hoare_partition(a, l, r)
        pivot = lomuto_partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)

n = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr)-1)
print(arr)