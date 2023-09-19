# 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
from collections import deque;
def merge(left, right):
    result = []

    # 병합과정
    # 각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
    # 두 부분집합에 요소가 없어질 때 까지 계속 반복
    l = r = 0
    while l < len(left) or r < len(right):
        # 두 부분집합의 요소가 모두 남아 있으면
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # 왼쪽만 남았을 때
        elif l < len(left):
            result.append(left[l]) #하나씩복사
            l += 1
            # 한번에 나머지를 뒤에 붙임
            # result.extend(left)
            # left.clear()
        elif r < len(right):
            result.append(right[r])
            r += 1

    return result


def merge_sort(a):
    # basis
    global count
    if len(a) == 1:
        return a
    # 유도파트
    # 문제를 절반으로 나누어서 각각을 정렬
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)
        if left[-1] > right[-1]:
            count += 1
        return merge(left, right)

T = int(input())
for test_case in range(1, T+1):
    count = 0
    N = int(input())
    A = list(map(int, input().split()))
    A = merge_sort(A)

    print(f'#{test_case} {A[N//2]} {count}')