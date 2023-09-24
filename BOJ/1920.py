def binaryfind(target):
    l = 0
    r = len(arr1)-1
    while l <= r:
        mid = (l + r) // 2

        # mid 값이 target 일때
        if arr1[mid] == target:
            return 1
        elif arr1[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return 0

N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, input().split()))

for i in range(len(arr2)):
    print(binaryfind(arr2[i]))