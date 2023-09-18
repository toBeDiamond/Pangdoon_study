# 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
def merge(left, right):
    result = []

    # 병합과정
    # 각각의 최소값을(가장 앞쪽 값)을 비교해서 더 작은 요소
    # 두 부분집합에 요소가 없어질 때 까지 계속 반복
    while left or right:
        # 두 부분집합으 요소가 모두 남아 있으면
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        #왼쪽만 붙임
        elif left:
            result.append(left.pop(0))   # 하나씩 복사
            # 한번에 나머지를 뒤에 붙임
            # result.extend(left)
            # left.clear()
        elif right:
            result.append(right.pop(0))
    return result


def merge_sort(a):
    # 문제를 절반으로 나누어서 각각을 해결
    # basis
    if len(a) == 1:
        return a
    # 유도파트
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


N = int(input())
A = list(map(int, input().split()))
A = merge_sort(A)
